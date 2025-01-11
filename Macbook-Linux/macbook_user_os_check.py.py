#!/usr/bin/env python3

# Created by Ranger (Dec 2024)
# Version 2.0.0

# --- Imports ---
import os
import subprocess
import platform

# --- Colors ---
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'

def get_username():
    """Gets the current user's username."""
    try:
        username = subprocess.check_output(['whoami']).decode().strip()
        return username
    except subprocess.CalledProcessError:
        return "Unknown User"

def check_os():
    """Checks the OS and reports if it's macOS."""
    os_name = platform.system()
    if os_name == "Darwin":
        return f"{GREEN}MacBook{NC}"
    else:
        return f"{RED}{os_name}{NC}"

def display_user_info():
    """Displays the user information within a block of "code"."""
    username = get_username()
    os_type = check_os()

    print(f"""
{YELLOW}--- System Information ---{NC}
    Operating System: {os_type}
    
{BLUE}Current User:{NC}
    {GREEN}
    ┌──────────────────────────────┐
    │  {username:<28}  │
    └──────────────────────────────┘
    {NC}
""")

display_user_info()