#!/usr/bin/env python3
# Created by Ranger

# This works on Windows only. 
# It checks if Visual Studio Code is installed on the system.

# Usage information
# python vs_code_install_check.py

# Adding the correct path to the Visual Studio Code executable is important.
# Make sure to replace the placeholder path with your actual Visual Studio Code path.
# You can search for code.cmd on your system to find the path.
# It is usually located in the "bin" directory of the installation path.
# My path is this "C:\Users\YOURNAME\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"

# This is what the code does:
# It checks if Visual Studio Code is installed on the system.
# The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
# The check_call function runs the command described by args. It will raise a CalledProcessError if the return code is non-zero.
# The FileNotFoundError exception is raised when a file or directory is requested but cannot be found.
# The is_vscode_installed function checks if Visual Studio Code is installed on the system.
# It uses the subprocess module to run the code.cmd --version command.
# If the command is successful, the function returns True. Otherwise, it returns False.
# The if __name__ == "__main__": block is used to check if the script is being run directly.
# If the script is run directly, it calls the is_vscode_installed function and prints the result.
# If Visual Studio Code is installed, it prints "Visual Studio Code is installed." Otherwise, it prints "Visual Studio Code is not installed."
# You can use this script to check if Visual Studio Code is installed on a Windows system.
# If you want to check for other operating systems, you may need to modify the script to use different commands or paths.

# Import the subprocess module to run the command line.
import subprocess

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

def is_vscode_installed():
    try:
        vscode_executable = r"C:\Users\david\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
        subprocess.check_call([vscode_executable, "--version"], shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
    except FileNotFoundError:
        print("Visual Studio Code executable not found.")
        return False

if __name__ == "__main__":
    if is_vscode_installed():
        print("Visual Studio Code is installed.")
    else:
        print("Visual Studio Code is not installed.")

input("Press Enter to exit...")