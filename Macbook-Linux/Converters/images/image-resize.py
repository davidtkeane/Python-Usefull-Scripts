#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
from PIL import Image
import os

def resize_image(input_image_path, output_image_path, output_format, size=(512, 512)):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Resize image
        resized_img = img.resize(size)
        
        # Save the resized image with the specified format
        if output_format.lower() in ['jpg', 'jpeg']:
            resized_img = resized_img.convert("RGB")  # Ensure RGB mode for .jpg
        resized_img.save(output_image_path, format=output_format.upper())

def get_output_path(input_image_path, output_format):
    # Remove extension and add desired format
    base_name = os.path.splitext(input_image_path)[0]
    return f"{base_name}_512x512.{output_format}"

if __name__ == "__main__":
    input_image = input("Enter the path to the image: ")
    output_format = input("Enter the desired output format (jpg, webp, png, gif): ").lower()

    # Determine the output image path
    output_image = get_output_path(input_image, output_format)

    # Call the function to resize the image
    try:
        resize_image(input_image, output_image, output_format)
        print(f"Image successfully resized and saved as {output_image}")
    except Exception as e:
        print(f"Error resizing the image: {e}")
