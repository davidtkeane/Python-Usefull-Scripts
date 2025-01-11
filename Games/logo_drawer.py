#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import requests
from PIL import Image
from io import BytesIO
import ascii_magic


# ascii_magic

def get_logo_image(search_term, api_key):
    headers = {"Ocp-Apim-Subscription-Key" : api_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get("https://api.bing.microsoft.com/v7.0/images/search", headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    first_result = search_results["value"][0]
    image_url = first_result["contentUrl"]
    return image_url

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    return image

def convert_image_to_ascii(image):
    output = ascii_magic.from_image(image)
    output = ascii_magic.to_terminal(output)
    return output

def main(search_term):
    api_key = 'YOUR_API_KEY_HERE'
    image_url = get_logo_image(search_term, api_key)
    image = download_image(image_url)
    ascii_art = convert_image_to_ascii(image)
    print(ascii_art)

if __name__ == '__main__':
    import sys
    try:
        search_term = sys.argv[1]
    except IndexError:
        print("Please provide a search term as an argument.")
        print("Usage: python logo_drawer.py <search_term>")
        print("Example: python logo_drawer.py python")
        search_term = "python"  # Default search term
    main(search_term)