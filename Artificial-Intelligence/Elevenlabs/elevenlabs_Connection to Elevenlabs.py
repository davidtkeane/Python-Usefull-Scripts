#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

# Import the subprocess module to run commands
import requests  # Import the requests library to make HTTP requests
import os  # Import os module to interact with the operating system

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 

# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/W9DtCotAanNkDo3mYyje"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "elevenlabs-api-key": "Add your API key here"
}

data = {
  "text": "If you can hear this then you have made the connection!!",  # Text to be converted into speech
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0.0,
    "use_speaker_boost": True
  }
}


# Send a POST request to the ElevenLabs API with the specified URL, headers, and data
response = requests.post(url, json=data, headers=headers)  

# Create a directory named 'test' if it doesn't exist to store the downloaded audio file
test_file_path = 'test' # Directory name
if not os.path.exists(test_file_path): # Check if the directory already exists
    os.makedirs(test_file_path) # Create the directory if it doesn't exist

# Create the path for the new file including the directory and file name
filename = os.path.join(test_file_path, 'elevenlabs_test.mp3')

# Open the file in binary write mode and write chunks of data into the file
with open(filename, 'wb') as f: # Open the file in binary write mode
  for chunk in response.iter_content(chunk_size=CHUNK_SIZE):  # Read the response in chunks
    if chunk:  # Check if the chunk has content
      f.write(chunk)  # Write the non-empty chunk to the file
print ("")
print('Connection to Elevenlabs successful!')  # Print a success message after playing the audio

