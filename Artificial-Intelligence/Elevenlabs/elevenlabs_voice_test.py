#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import requests
import os

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 

# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

# Define constants for the script
CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
ELEVENLABS_API_KEY = "Add Your Own ElevenLabs API Key Here"  # Your API key for authentication
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # ID of the voice model to use
TEXT_TO_SPEAK = "Hello There you sexy thing ya!"  # Text you want to convert to speech
OUTPUT_PATH = "test/output.mp3"  # Path to save the output audio file

# Construct the URL for the Text-to-Speech API request
tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

# Set up headers for the API request, including the API key for authentication
headers = {
    "Accept": "application/json",
    "elevenlabs-api-key": ELEVENLABS_API_KEY
}

data = {
    "text": TEXT_TO_SPEAK,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
  }
}

# Make the POST request to the TTS API with headers and data, enabling streaming response
response = requests.post(tts_url, headers=headers, json=data, stream=True)

# Check if the request was successful
if response.ok:
    # Open the output file in write-binary mode
    with open(OUTPUT_PATH, "wb") as f:
        # Read the response in chunks and write to the file
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
    # Inform the user of success
    print("Audio stream saved successfully.")
else:
    # Print the error message if the request was not successful
    print(response.text)