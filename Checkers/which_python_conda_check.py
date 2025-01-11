#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python which_python_conda_check.py

# This is what the code does:
# This script checks if Python and Anaconda are installed and offers to install or update them if necessary.
# It also checks for pip and offers to upgrade it if it's installed.
# The script is written in Python and should work on Windows, macOS, and Linux.
# The run_command function executes a command and returns its output.
# The check_command function verifies if a command exists.
# The get_version function gets the version of a program.
# The upgrade_packages function attempts to upgrade pip and python packages to the latest versions using pip.
# The offer_python_installation function prompts the user to install Python if it's not present.
# The offer_anaconda_installation function prompts the user to install Anaconda if desired.
# The main function checks installations and offers updates or installs.
# The if __name__ == '__main__': block is used to check if the script is being run directly.
# If the script is run directly, it calls the main function.

# Import the subprocess module to run commands
# Import the sys module to access command-line arguments
# Import the os module to access the operating system
# Import the platform module to access the operating system information
# Import the psutil module to access system information

import subprocess
import sys

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

# Function to execute a command and return its output
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

# Function to verify if a command exists
def check_command(command):
    _, _, return_code = run_command(command)
    return return_code == 0

# Function to get the version of a program
def get_version(command):
    version_output, _, _ = run_command(command + ["--version"])
    return version_output

# Function to attempt upgrading pip and python packages to the latest versions using pip
def upgrade_packages(python_exe):
    print(f"\nUpgrading pip for {python_exe}...")
    run_command([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])
    # Add any other package you want to upgrade here, for example:
    # run_command([python_exe, '-m', 'pip', 'install', '--upgrade', 'package_name'])

# Function to prompt the user to install Python if it's not present
def offer_python_installation():
    print("\nPython is NOT installed.")
    install_python = input("Do you want to install Python now? (yes/no): ")
    if install_python.lower() == 'yes':
        print("Please visit https://www.python.org/downloads/ to download and install Python.")
    else:
        print("Python installation was skipped by user.")

# Function to prompt the user to install Anaconda if desired
def offer_anaconda_installation():
    install_anaconda = input("\nDo you want to install Anaconda as well? (yes/no): ")
    if install_anaconda.lower() == 'yes':
        print("Please visit https://www.anaconda.com/products/distribution to download and install Anaconda.")
    else:
        print("Anaconda installation was skipped by user.")

# Main function to check installations and offer updates or installs
def main():
    python_installed = check_command(['where', 'python'])
    pip_installed = check_command(['where', 'pip'])

    if python_installed:
        print("Python is installed")
        if pip_installed:
            print("pip is installed")
        else:
            print("pip is NOT installed")

        # Get all Python executables
        python_executables, _, _ = run_command(['where', 'python'])
        python_versions = {}
        for python_exe in python_executables.splitlines():
            python_version = get_version([python_exe])
            python_versions[python_exe] = python_version
            print(f"{python_exe}: {python_version}")
            if pip_installed:
                upgrade_packages(python_exe)
    else:
        offer_python_installation()

    anaconda_installed = check_command(['conda', 'info'])
    if anaconda_installed:
        print("\nAnaconda is installed")
        print(get_version(['conda']))
        # Offer to update Anaconda if necessary:
        # run_command(['conda', 'update', '--all', '--yes'])
    else:
        miniconda_installed = check_command(['conda', 'info'])
        if miniconda_installed:
            print("\nMiniconda is installed")
            print(get_version(['conda']))
            # Offer to update Miniconda if necessary:
            # run_command(['conda', 'update', '--all', '--yes'])
    
    if not (anaconda_installed or miniconda_installed) and not python_installed:
        offer_anaconda_installation()

if __name__ == '__main__':
    main()
