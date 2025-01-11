#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version 1.0.0
# Created by Ranger 😎

# This script formats Python code files (.py) within the given directory or a single file using autopep8.
# Usage: python format_code.py <target>

# Importing required modules
import os
import sys
import subprocess

def format_python_code(target):
    """
    Formats Python code files (.py) within the given directory or a single file using autopep8.

    Args:
        target (str): The path to a directory containing Python files, or a specific Python file.
    """
    if os.path.isfile(target) and target.endswith(".py"):
      try:
         # autopep8 is run and also in place change that file with agressive output
         subprocess.run(["autopep8", "--in-place", "--aggressive", target], check=True)
         print(f"Formatted: {target}")
      except subprocess.CalledProcessError as e:
          print(f"Error formatting {target}: {e}")
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    try:
                         # autopep8 is run and also in place change that files and all sub folders in that directory
                        subprocess.run(["autopep8", "--in-place", "--aggressive", filepath], check=True)
                        print(f"Formatted: {filepath}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error formatting {filepath}: {e}")

    else:
         print ("Not a file or valid folder, chose a specific file or a folder using '.'")
         print_help()
def print_help():
    print("""
Usage: python format_code.py <target>

Where <target> can be:

*  a single Python file path. Example: python format_code.py chess_combined.py
*  a directory path with .py python files. Example: python format_code.py .

Packages and functionality in the current version:

    autopep8 : Used as main formatter, to correct styles, and format based on PEP8, with spacing and remove redundencies. The in place command will alter the files in directory or single file location.
""")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python format_code.py <file or directory>")
        print_help()
        sys.exit(1)
    target = sys.argv[1]
    format_python_code(target)
    print("Format is complete.")