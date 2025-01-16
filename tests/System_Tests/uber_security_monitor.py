import psutil
import time
import datetime
import os
import json
import subprocess
from pync import Notifier
import re

class SecurityMonitor:
    def __init__(self):
        self.monitored_processes = {'ssh', 'ping', 'nc', 'nmap'}
        self.suspicious_ports = {22, 23, 3389, 5900}
        self.log_file = 'security_monitor_log.txt'
        self.config_file = 'security_config.json'
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'monitored_processes': list(self.monitored_processes),
                'suspicious_ports': list(self.suspicious_ports),
                'alert_threshold': 5
            }
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def check_processes(self):
        for proc in psutil.process_iter(['name', 'pid', 'cmdline']):
            try:
                if proc.info['name'].lower() in self.config['monitored_processes']:
                    if proc.info['name'].lower() == 'ssh':
                        ssh_details = self.extract_ssh_details(proc.info['cmdline'])
                        return proc.info['name'], proc.info['pid'], ssh_details
                    elif proc.info['name'].lower() == 'ping':
                        ip_address = self.extract_ip_from_ping(proc.info['cmdline'])
                        return proc.info['name'], proc.info['pid'], ip_address
                    return proc.info['name'], proc.info['pid'], None
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return None, None, None

    def extract_ssh_details(self, cmdline):
        if not cmdline:
            return "Unknown SSH command"
        
        ssh_command = ' '.join(cmdline)
        port = "22"  # Default SSH port
        user = "Unknown"
        host = "Unknown"
        
        # Extract port if specified
        port_match = re.search(r'-p\s+(\d+)', ssh_command)
        if port_match:
            port = port_match.group(1)
        
        # Extract user and host
        user_host_match = re.search(r'(\w+@)?([^\s]+)$', ssh_command)
        if user_host_match:
            if user_host_match.group(1):
                user = user_host_match.group(1)[:-1]  # Remove the '@' symbol
            host = user_host_match.group(2)
        
        return f"User: {user}, Host: {host}, Port: {port}"

    def extract_ip_from_ping(self, cmdline):
        if cmdline and len(cmdline) > 1:
            potential_ip = cmdline[-1]
            ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            match = re.search(ip_pattern, potential_ip)
            if match:
                return match.group()
        return "Unknown"

    def check_open_ports(self):
        try:
            output = subprocess.check_output("lsof -i -P -n | grep LISTEN", shell=True).decode()
            open_ports = set()
            for line in output.split('\n'):
                if line:
                    parts = line.split()
                    if len(parts) > 8:
                        port = parts[8].split(':')[-1]
                        if port.isdigit():
                            open_ports.add(int(port))
            return open_ports.intersection(set(self.config['suspicious_ports']))
        except subprocess.CalledProcessError:
            return set()

    def log_event(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as log_file:
            log_file.write(f"{timestamp}: {message}\n")

    def monitor(self):
        alert_count = 0
        while True:
            proc_name, proc_id, details = self.check_processes()
            suspicious_ports = self.check_open_ports()

            if proc_name or suspicious_ports:
                alert_count += 1
                if proc_name:
                    if proc_name.lower() == 'ssh':
                        message = f"SSH process detected (PID: {proc_id}). Details: {details}"
                    elif proc_name.lower() == 'ping':
                        message = f"PING process detected (PID: {proc_id}) to IP: {details}"
                    else:
                        message = f"{proc_name.upper()} process detected (PID: {proc_id})"
                else:
                    message = f"Suspicious ports detected: {suspicious_ports}"

                self.log_event(message)
                Notifier.notify(message, title="Security Alert")

                if alert_count >= self.config['alert_threshold']:
                    self.log_event("Alert threshold reached. Performing system scan...")
                    self.perform_system_scan()
                    alert_count = 0

            time.sleep(10)

    def perform_system_scan(self):
        # Placeholder for system scan
        self.log_event("System scan completed.")

def main():
    monitor = SecurityMonitor()
    monitor.monitor()

if __name__ == "__main__":
    main()