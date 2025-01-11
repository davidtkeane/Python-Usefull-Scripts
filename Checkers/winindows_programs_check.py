#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
import platform
import subprocess

def get_installed_programs():
    system = platform.system()
    if system != "Windows":
        print("Unsupported operating system")
        return

    reg_keys = [
        r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
        r'HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
    ]
    programs = []

    for key in reg_keys:
        try:
            output = subprocess.check_output(f'reg query {key} /s /v DisplayName', shell=True, text=True, stderr=subprocess.STDOUT, timeout=300)
            programs.extend([line.split('REG_SZ')[-1].strip() for line in output.splitlines() if 'DisplayName' in line])
        except subprocess.CalledProcessError as e:
            print(f"Error while executing command: {key}\nError output: {e.output}")
        except subprocess.TimeoutExpired:
            print("Command execution timed out. Please try again.")

    try:
        output = subprocess.check_output('powershell "Get-AppxPackage -AllUsers | Select-Object Name"', shell=True, text=True, stderr=subprocess.STDOUT, timeout=300)
        programs.extend([line.strip() for line in output.splitlines() if line and 'Name' not in line])
    except subprocess.CalledProcessError as e:
        print(f"Error while executing command: {cmd2}\nError output: {e.output}")
    except subprocess.TimeoutExpired:
        print("Command execution timed out. Please try again.")

    return '\n'.join(sorted(set(programs)))

if __name__ == "__main__":
    programs = get_installed_programs()
    if programs:
        with open("programs.txt", "w") as f:
            f.write(programs)
        print("List of installed programs saved to 'programs.txt'")
    else:
        print("No programs found.")
py