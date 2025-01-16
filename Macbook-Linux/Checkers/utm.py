#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import subprocess

def check_disk_format(disk_name):
    result = subprocess.run(['diskutil', 'info', disk_name], capture_output=True, text=True)
    if result.returncode != 0:
        return "Error: Disk not found"
    if "APFS" in result.stdout or "Mac OS Extended" in result.stdout:
        return "Disk format is compatible"
    else:
        return "Disk format is not compatible"

# Replace 'disk2s1' with the identifier of your external HDD
print(check_disk_format('disk2s1'))
