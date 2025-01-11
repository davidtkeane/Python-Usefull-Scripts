#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
import time
from datetime import datetime, timedelta
import cv2
import schedule

# Set the interval for taking photos (in seconds)
interval = 60 * 1 # e.g., 1 minute
start_time = datetime(2023, 4, 15, 10, 30) # set start time to future date and time
while True:
    current_time = datetime.now()
    elapsed_time = (current_time - start_time).total_seconds()
    
    if elapsed_time > interval:
        print("Taking photo...")
        # Set the camera resolution (e.g., 1920x1080) and framerate (e.g., 30 fps)
        cap = cv2.VideoCapture(0)
        
        # Take a photo with the camera
        ret, frame = cap.read()
        if ret:
            print("Photo taken on", current_time)
            # Save the image to disk (e.g., in a folder named 'photos')
            filename = f"photo_{current_time:%Y-%m-%d_%H-%M-%S}.jpg"
            cv2.imwrite(filename, frame)
        else:
            print("Error taking photo")
    # Wait for the next interval before taking another photo
    time.sleep(1)