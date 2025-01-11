#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python Apple_Macbook_MPS/check_mps_torch_availability.py

# This is what the code does:
# 1. Check the availability of the MPS device
# 2. Determine the best available device (MPS or CPU)
# 3. Print the active device to the console


# Import the torch module
import torch

def check_mps_availability():
    # Check MPS availability
    mps_available = torch.backends.mps.is_available()
    mps_built = torch.backends.mps.is_built()
    
    print(f"MPS Available: {mps_available}")
    print(f"MPS Built: {mps_built}")
    
    # Determine best available device
    if mps_available and mps_built:
        device = torch.device("mps")
        print("Using MPS device")
    else:
        device = torch.device("cpu")
        print("Using CPU device")
        
    return device

if __name__ == "__main__":
    device = check_mps_availability()
    print(f"\nActive Device: {device}")