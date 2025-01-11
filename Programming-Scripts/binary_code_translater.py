#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import pyfiglet

def text_to_binary():
    # Generate a banner
    banner = pyfiglet.figlet_format("Text to Binary Converter")
    print(banner)

    # Ask the user for a word or sentence
    text = input("Please enter a word or sentence: ")

    # Convert the text to binary
    binary = ' '.join(format(ord(char), '08b') for char in text)

    # Print the result
    print("\nHere is your text in binary:")
    print(binary)

# Run the function
text_to_binary()