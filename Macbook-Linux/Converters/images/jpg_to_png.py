#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
from PIL import Image, ExifTags

def convert_image_format(img_path, target_format):
    img = Image.open(img_path)

    # Handle EXIF orientation metadata
    if hasattr(img, '_getexif'): 
        exif = img._getexif()
        if exif is not None:
            for tag, value in exif.items():
                if tag in ExifTags.TAGS and ExifTags.TAGS[tag] == 'Orientation':
                    if value == 3: 
                        img = img.rotate(180, expand=True)
                    elif value == 6: 
                        img = img.rotate(270, expand=True)
                    elif value == 8:
                        img = img.rotate(90, expand=True)
                    break

    img.save('output_image.'+target_format, target_format)

convert_image_format('rangers_ship_at_port.png', 'png')