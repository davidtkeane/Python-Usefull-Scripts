#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
import argparse

# Add command line argument for specifying folder
parser = argparse.ArgumentParser(description="Search for Python files in a directory.")
parser.add_argument('--folder', type=str, default="C:/", help="Folder path to search in.")
args = parser.parse_args()
folderToSearch = args.folder

# Function to find and write .py files to a text file
def find_py_files(folder):
    try:
        with open("pyFiles.txt", "w") as pyFiles:
            # Iterate through all files and subfolders in the folder
            for root, dirs, files in os.walk(folder):
                for fileName in files:
                    # Check if the file is a .py file
                    if fileName.endswith('.py'):
                        full_path = os.path.join(root, fileName)
                        print(f"Found: {full_path}")
                        # Write the .py file name and full path to .txt file
                        pyFiles.write(full_path + '\n')
    except PermissionError:
        print("Permission Denied: Make sure you have the appropriate permissions to read the directory and write to a file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
find_py_files(folderToSearch)
