#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
from pydub import AudioSegment
from tkinter import Tk, filedialog
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ffmpeg_installed():
    try:
        from pydub.utils import which
        if which("ffmpeg") is None:
            raise EnvironmentError("FFmpeg not found. Please install FFmpeg and add it to your PATH.")
        if which("ffprobe") is None:
            raise EnvironmentError("FFprobe not found. Please install FFmpeg and add it to your PATH.")
    except Exception as e:
        logging.error(e)
        raise e

def convert_audio(input_file, output_file):
    try:
        # Detect the file format from the input file
        file_format = input_file.split('.')[-1].lower()
        
        logging.info(f"Reading input file: {input_file}")
        audio = AudioSegment.from_file(input_file, format=file_format)
        
        # Detect the output format from the output file
        output_format = output_file.split('.')[-1].lower()
        
        logging.info(f"Converting {file_format.upper()} to {output_format.upper()}")
        audio.export(output_file, format=output_format)
        
        logging.info(f"Conversion completed: {output_file}")
        print("Conversion completed successfully!")
    except Exception as e:
        logging.error(f"Error during conversion: {e}")
        print(f"Error during conversion: {e}")

def select_file():
    Tk().withdraw()  # Close the root window
    file_path = filedialog.askopenfilename()
    return file_path

def save_file(default_name):
    Tk().withdraw()  # Close the root window
    save_path = filedialog.asksaveasfilename(defaultextension=".wav", initialfile=default_name)
    return save_path

def main():
    print("Welcome to the Audio Converter!")
    print("Select the conversion type:")
    print("1: MP3 to WAV")
    print("2: WAV to MP3")
    print("3: FLAC to MP3")
    print("4: MP3 to FLAC")
    print("5: OGG to MP3")
    print("6: AAC to MP3")
    print("7: Other")

    choice = input("Enter your choice (1-7): ")

    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice. Exiting.")
        return

    # File type conversion options
    conversion_options = {
        '1': ('mp3', 'wav'),
        '2': ('wav', 'mp3'),
        '3': ('flac', 'mp3'),
        '4': ('mp3', 'flac'),
        '5': ('ogg', 'mp3'),
        '6': ('aac', 'mp3')
    }

    if choice == '7':
        source_format = input("Enter the source format (e.g., mp3, wav, flac): ").lower()
        target_format = input("Enter the target format (e.g., mp3, wav, flac): ").lower()
    else:
        source_format, target_format = conversion_options[choice]

    print("Please select the file to convert.")
    input_file = select_file()
    
    if not input_file:
        print("No file selected. Exiting.")
        return
    
    default_name = f"converted.{target_format}"
    print("Please select the location to save the converted file.")
    print(f"Press Enter to save in the current directory with the name {default_name}.")
    save_path = save_file(default_name)

    if not save_path:
        save_path = os.path.join(os.getcwd(), default_name)
    
    print(f"Saving converted file to: {save_path}")
    try:
        check_ffmpeg_installed()
        convert_audio(input_file, save_path)
    except EnvironmentError as e:
        print(e)

if __name__ == "__main__":
    main()
