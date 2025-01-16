#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

payload = {
    "text": "<string>",
    "model_id": "<string>",
    "language_code": "<string>",
    "voice_settings": {
        "stability": 123,
        "similarity_boost": 123,
        "style": 123,
        "use_speaker_boost": True
    },
    "pronunciation_dictionary_locators": [
        {
            "pronunciation_dictionary_id": "<string>",
            "version_id": "<string>"
        }
    ],
    "seed": 123,
    "previous_text": "<string>",
    "next_text": "<string>",
    "previous_request_ids": ["<string>"],
    "next_request_ids": ["<string>"]
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)