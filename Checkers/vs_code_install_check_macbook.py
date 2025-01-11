#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import subprocess
import os

# Check if Visual Studio Code is installed
def is_vscode_installed():
    try:
        subprocess.check_output(["code", "--version"])
        return True
    except FileNotFoundError:
        return False

# Check Python files in the current directory for syntax errors and run them
def check_and_run_python_files():
    python_files = [file for file in os.listdir() if file.endswith(".py")]
    if not python_files:
        print("No Python files found in the current directory.")
        return

    for python_file in python_files:
        print(f"Checking and running {python_file}:")
        try:
            # Check for syntax errors
            subprocess.check_output(["python", "-m", "py_compile", python_file], stderr=subprocess.STDOUT)
            print(f"No syntax errors found in {python_file}.\nRunning {python_file}:\n")
            # Run the Python file
            subprocess.run(["python", python_file], check=True)
            print(f"\n{python_file} executed successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"Syntax errors or execution issues in {python_file}:\n{e.output.decode()}\n")

if __name__ == "__main__":
    if is_vscode_installed():
        print("Visual Studio Code is installed.")
    else:
        print("Visual Studio Code is not installed.")

    check_and_run_python_files()
