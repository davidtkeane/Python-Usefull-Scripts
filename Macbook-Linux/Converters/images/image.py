#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
user_id = "user-1234"

# Generate an image using OpenAI's DALL-E API
# --- Generate Image ---
response = client.images.generate(
  model="dall-e-3",
  prompt="A picture of the A-Team, with makup on their faces sitting in the van",
  n=1,
  size="1024x1024",
  response_format="url"
)

print(response)

for i, image_data in enumerate(response.data, start=1):
    url = image_data.url  # Access the url attribute directly
    image_content = requests.get(url).content
    with open(f'image_{i}.jpg', 'wb') as f:
        f.write(image_content)

