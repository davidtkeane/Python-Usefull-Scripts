#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Usage: python honeybadger_check.py

# Import necessary libraries
# --- Imports ---
import os
import sys
import subprocess
from typing import Tuple

def check_espeak_version(espeak_path: str = 'espeak') -> Tuple[bool, str]:
    """
    Check if espeak is installed and get version
    Returns: Tuple of (success, version/error message)
    """
    try:
        env = os.environ.copy()
        env['PATH'] += ':/opt/homebrew/bin'
        result = subprocess.run(
            [espeak_path, '--version'], 
            capture_output=True, 
            text=True,
            env=env
        )
        return True, result.stdout
    except Exception as e:
        return False, f"Error checking espeak: {str(e)}"

def test_espeak_speech(text: str = "Hello World!") -> Tuple[bool, str]:
    """
    Test espeak speech synthesis
    Returns: Tuple of (success, message)
    """
    try:
        process = subprocess.Popen(
            ['espeak', '-v', 'en-us', text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        _, stderr = process.communicate()
        if process.returncode == 0:
            return True, "Speech synthesis successful"
        return False, f"Error: {stderr.decode()}"
    except Exception as e:
        return False, f"Error with speech synthesis: {str(e)}"

def print_python_info():
    """Print Python environment information"""
    print(f"Python Executable: {sys.executable}")
    print(f"Python Prefix: {sys.prefix}")

def main():
    # Check espeak version
    success, version = check_espeak_version('/opt/homebrew/bin/espeak')
    if success:
        print(f"eSpeak Version:\n{version}")
    else:
        print(version)

    # Test speech synthesis
    success, message = test_espeak_speech()
    print(message)

    # Print Python environment info
    print("\nPython Environment Information:")
    print_python_info()

if __name__ == "__main__":
    main()