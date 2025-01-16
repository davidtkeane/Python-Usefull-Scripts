#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import socket

def test_ipv4():
    try:
        # Create an IPv4 socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        # Attempt to connect to Google's public DNS server on port 53
        s.connect(("8.8.8.8", 53))
        s.close()
        print("IPv4 is working.")
    except Exception as e:
        print("IPv4 is not working. Error:", e)

def test_ipv6():
    try:
        # Create an IPv6 socket object
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.settimeout(5)
        # Attempt to connect to Google's public DNS server on port 53
        s.connect(("2001:4860:4860::8888", 53))
        s.close()
        print("IPv6 is working.")
    except Exception as e:
        print("IPv6 is not working. Error:", e)

# Test IPv4 and IPv6
test_ipv4()
test_ipv6()
