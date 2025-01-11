#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
import sys
import torch

# Check if MPS device is available on the system
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print ("MPS device available.")
    print ("The output should show below: tensor([1.], device='mps:0')")
    print("")
    print (x)
else:
    print ("MPS device not found.")

# The output should show:
# tensor([1.], device='mps:0')