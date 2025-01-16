#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import platform
import psutil
import os


# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

# get operating system information
print("Operating System:")
print(platform.system())
print(platform.release())

# get CPU information
print("\nCPU:")
print(platform.processor())

# get RAM information
print("\nRAM:")
print(str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB")
