#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import subprocess
import os
import sys

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output.strip().split('\n')
    except subprocess.CalledProcessError as e:
        return None

def check_python_installations():
    paths = run_command("where python")
    if paths:
        for path in paths:
            print(f"Python found at: {path}")
            try:
                python_version = subprocess.check_output([path, "--version"], text=True).strip()
                print(f"Version: {python_version}")
            except subprocess.CalledProcessError:
                print("Error getting Python version")
    else:
        print("Python is not installed or not in PATH")

def check_pip_installation():
    pip_path = run_command("where pip")
    if pip_path:
        print(f"pip found at: {pip_path[0]}")
        try:
            pip_version = subprocess.check_output([pip_path[0], "--version"], text=True).strip()
            print(f"pip version: {pip_version}")
        except subprocess.CalledProcessError:
            print("Error getting pip version")
    else:
        print("pip is not installed or not in PATH")

def check_conda_installations():
    conda_path = run_command("where conda")
    if conda_path:
        for path in conda_path:
            print(f"Conda found at: {path}")
            try:
                conda_info = subprocess.check_output([path, "info"], text=True).strip()
                print(conda_info)
            except subprocess.CalledProcessError:
                print("Error getting Conda info")
    else:
        print("Conda is not installed or not in PATH")

if __name__ == "__main__":
    print("Checking for Python installations...")
    check_python_installations()

    print("\nChecking for pip installation...")
    check_pip_installation()

    print("\nChecking for Conda installations...")
    check_conda_installations()
