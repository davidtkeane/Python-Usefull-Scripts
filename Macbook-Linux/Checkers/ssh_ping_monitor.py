#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

import psutil
import time
from pync import Notifier
import datetime

def check_processes(monitored_processes):
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'].lower() in monitored_processes:
            return proc.info['name'], proc.info['pid']
    return None, None

def main():
    monitored_processes = {'ssh', 'ping'}
    
    while True:
        proc_name, proc_id = check_processes(monitored_processes)
        
        if proc_name:
            message = f"{proc_name.upper()} connection detected (PID: {proc_id})"
            Notifier.notify(message, title="Connection Alert")
            
            # Log the event
            with open('connection_log.txt', 'a') as log_file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp}: {message}\n")
        
        time.sleep(10)  # Check every 60 seconds

if __name__ == "__main__":
    main()