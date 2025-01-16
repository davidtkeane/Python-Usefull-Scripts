#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import subprocess

def check_command(command):
    try:
        subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False

def check_registry_key(registry_key):
    return check_command(['reg', 'query', registry_key])

def get_python_installation_locations():
    output = subprocess.check_output(['where', 'python'])
    python_installations = output.decode('utf-8').split('\n')
    return python_installations

def get_anaconda_installation_location():
    registry_key = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{9FFD80C8-130D-11D2-88FA-00A0C90F575D}'
    if check_registry_key(registry_key):
        install_location = subprocess.check_output(['reg', 'query', registry_key, '/v', 'InstallLocation'])
        install_location = install_location.decode('utf-8').split('\r\n')[1].split('REG_SZ ')[-1]
        return install_location
    else:
        return None

def get_miniconda_installation_location():
    registry_key = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{82A2294B-B7A2-443C-838D-7024E1E1A2E1}'
    if check_registry_key(registry_key):
        install_location = subprocess.check_output(['reg', 'query', registry_key, '/v', 'InstallLocation'])
        install_location = install_location.decode('utf-8').split('\r\n')[1].split('REG_SZ ')[-1]
        return install_location
    else:
        return None

if __name__ == '__main__':
    python_installed = check_command(['where', 'python'])
    pip_installed = check_command(['where', 'pip'])

    if python_installed:
        print("Python is installed")
        if pip_installed:
            print("pip is installed")
            python_locations = get_python_installation_locations()
            if len(python_locations) > 1:
                print("Multiple Python versions are installed")
                print("Python Locations:")
                for location in python_locations:
                    print(location)

    anaconda_installed = check_registry_key(r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{9FFD80C8-130D-11D2-88FA-00A0C90F575D}')
    if anaconda_installed:
        print("Anaconda is installed")
        anaconda_location = get_anaconda_installation_location()
        if anaconda_location:
            print("Anaconda Location:", anaconda_location)
        else:
            print("Anaconda installation location not found")

    miniconda_installed = check_registry_key(r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{82A2294B-B7A2-443C-838D-7024E1E1A2E1}')
    if miniconda_installed:
        print("Miniconda is installed")
        miniconda_location = get_miniconda_installation_location()
        if miniconda_location:
            print("Miniconda Location:", miniconda_location)
        else:
            print("Miniconda installation location not found")