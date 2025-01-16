#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

# Powershell script to display a notification

import subprocess

# Define the message to display in the notification
message = "Hello!"

# Execute the command to display the notification
subprocess.run(["osascript", "-e", f'display notification "{message}" with title "Notification"'])

# Please note that the PowerShell script requires the .NET Framework to be installed on the system.
