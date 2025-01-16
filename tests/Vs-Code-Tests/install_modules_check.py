#!/usr/bin/env python3
# Created by Ranger

# This works on Windows only. It checks if Visual Studio Code is installed on the system.
# This is a Python script that checks and installs required modules for the project.

# Usage information
# python install_modules_check.py

# How this script works:
# This script checks if the required modules are installed and installs them if they are not.
# The script requires an active internet connection to install the modules.
# The script uses the subprocess module to run shell commands and manage child processes.
# The script uses the sys module to access variables used or maintained by the Python interpreter and to interact with the interpreter.
# The script uses the os module to interact with the operating system, including file operations and environment variables.

# Import required modules
import subprocess
import sys

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_package(package):
    try:
        dist = __import__(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed.")
        user_input = input(f"Do you want to install {package}? (Y/N): ").strip().upper()
        if user_input == "Y":
            install_package(package)
            print(f"{package} has been successfully installed.")
        elif user_input == "N":
            print(f"Installation of {package} canceled by the user.")
        else:
            print("Unrecognized input. Please enter 'Y' to install or 'N' to cancel.")

def check_packages(packages):
    for package in packages:
        check_package(package)

def check_burnt_toast_module():
    try:
        # Check if the BurntToast module is available
        ps_command = "Get-Module -ListAvailable -Name BurntToast"
        result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        
        if "BurntToast" not in result.stdout:
            # Ask the user if they want to install the BurntToast module
            user_input = input("The BurntToast module is not installed. Do you want to install it? (Y/N): ").strip().upper()
            if user_input == "Y":
                try:
                    # Install the BurntToast module without prompting
                    install_command = "Install-Module -Name BurntToast -Scope CurrentUser -Force -Confirm:$false"
                    subprocess.run(["powershell", "-Command", install_command], check=True)
                    print("BurntToast module has been successfully installed.")
                except subprocess.CalledProcessError:
                    print("An error occurred during installation.")
                    return
            elif user_input == "N":
                print("Installation canceled by the user.")
                return
            else:
                print("Unrecognized input. Please enter 'Y' to install or 'N' to cancel.")
                return
        else:
            print("BurntToast module is already installed.")
    
    except subprocess.SubprocessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    packages = ["pyttsx3", "speech_recognition", "openai", "requests", "pymongo", "pydub", "pyaudio", "wave"]
    check_packages(packages)
    check_burnt_toast_module()