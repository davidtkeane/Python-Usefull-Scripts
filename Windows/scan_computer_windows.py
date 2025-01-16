#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# pip install fsutil (Windows only)

# Import necessary libraries
# --- Imports ---
import subprocess
import os
import socket
import platform
import re

# Define the function to get the free space and installed software
def get_system_info():
    # Get the free space on the C drive
    free_space = subprocess.check_output(["fsutil", "volume", "diskfree", "C:"]).decode("utf-8")
    # Get the list of installed software
    software = subprocess.check_output(["wmic", "product", "get", "name,version"]).decode("utf-8", errors="ignore")
    # Get the list of installed drivers
    drivers = subprocess.check_output(["driverquery", "/v"]).decode("utf-8", errors="ignore")
    # Get the hostname
    hostname = socket.gethostname()
    # Get the operating system version
    os_version = platform.version()
    # Get the processor architecture
    processor_arch = platform.machine()
    # Get the system uptime
    uptime = subprocess.check_output(["systeminfo"]).decode("utf-8", errors="ignore")
    # Get the system load average
    load_average = subprocess.check_output(["wmic", "cpu", "get", "loadpercentage"]).decode("utf-8", errors="ignore")
    # Get the number of CPU cores
    num_cores = os.cpu_count()
    # Get the memory usage
    mem_usage = subprocess.check_output(["wmic", "memorychip", "get", "capacity"]).decode("utf-8", errors="ignore")
    # Get the network interfaces
    network_interfaces = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8", errors="ignore")

    # Compile the regular expression pattern to extract the version numbers from the software list
    version_pattern = re.compile(r"(\d+\.\d+\.\d+)")

    # Extract the version numbers from the software list
    software_versions = {}
    for line in software.splitlines():
        if "Name" in line:
            package_info = line.split()
            package_name = package_info[0]
            version_match = version_pattern.search(line)
            if version_match:
                version = version_match.group(1)
                software_versions[package_name] = version

    # Return the system information
    return {
        "free_space": free_space,
        "software": software_versions,
        "drivers": drivers,
        "hostname": hostname,
        "os_version": os_version,
        "processor_arch": processor_arch,
        "uptime": uptime,
        "load_average": load_average,
        "num_cores": num_cores,
        "mem_usage": mem_usage,
        "network_interfaces": network_interfaces
    }

# Get the system information
system_info = get_system_info()

# Print the system information
for key, value in system_info.items():
    print(f"{key}: {value}")