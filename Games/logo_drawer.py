#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from PIL import Image
from io import BytesIO
import ascii_magic
from dotenv import load_dotenv
from datetime import datetime
from honeybadger import honeybadger
from duckduckgo_search import DDGS
import tempfile

# --- Configuration ---
load_dotenv()

HONEYBADGER_API_KEY = os.getenv('HONEYBADGER_API_KEY', 'your_test_api_key')
BING_API_KEY = os.getenv('BING_API_KEY', 'your_bing_api_key')


honeybadger.configure(api_key=HONEYBADGER_API_KEY, environment='logo_drawer', force_report_data=True)

def check_honeybadger_connection():
    """Checks if the Honeybadger API key is configured and notifies the user."""
    if HONEYBADGER_API_KEY == 'your_test_api_key':
        print("Warning: Using default Honeybadger API key. Set HONEYBADGER_API_KEY in .env file for production use.")
        return False
    else:
        try:
             # Attempt a basic notification to test the connection
            honeybadger.notify("Honeybadger connection test")
            print(f"\033[92mHoneybadger API linked successfully ✅\033[0m")  # Green checkmark
            return True
        except Exception as e:
            print(f"Error linking Honeybadger API: {e}")
            return False


# --- Helper Functions ---

def get_search_engine():
    while True:
        print("\nChoose search engine:")
        print("1. Bing (Azure Cognitive Services)")
        print("2. DuckDuckGo")
        choice = input("Enter choice (1 or 2): ")
        if choice in ('1', '2'):
            return choice

def get_search_type():
    while True:
        print("\nChoose search type:")
        print("1. General image")
        print("2. Company logo")
        choice = input("Enter choice (1 or 2): ")
        if choice in ('1', '2'):
            return choice

def search_image(search_term, search_engine, search_type):
    print(f"\nStage 1: Searching for '{search_term}'...")
    try:
        if search_engine == '1':
            image_url = get_bing_image(search_term, BING_API_KEY, search_type == '2')
        else:
            image_url = get_duckduckgo_image(search_term, search_type == '2')
        print(f"Found image URL: {image_url}")
        return image_url
    except Exception as e:
        honeybadger.notify(e, context={'search_term': search_term, 'search_engine': search_engine})
        print(f"Error searching for image: {e}")
        return None

def download_image(url, search_term):
    print(f"\nStage 2: Downloading image...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data).convert("RGB")

        base_dir = os.path.dirname(__file__)
        image_dir = os.path.join(base_dir, 'images')
        os.makedirs(image_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = os.path.join(image_dir, f"{search_term}_{timestamp}.png")
        image.save(image_path)
        print(f"Image saved to: {image_path}")

         # Create temp file and copy image to it
        temp_image = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        image.save(temp_image.name)
        temp_image.close() #Close the temp file to access it later

        return image_path, temp_image.name  # Return both: original path and temp path

    except Exception as e:
        honeybadger.notify(e, context={'url': url, 'search_term': search_term})
        print(f"Error downloading image: {type(e).__name__}: {e}")
        return None, None


def convert_to_ascii(image_path, temp_image_path, search_term):
    print(f"\nStage 3: Converting to ASCII art...")
    try:
        #Load image from temp path
        image = Image.open(temp_image_path)

        aspect_ratio = image.width / image.height
        new_width = 80
        new_height = int(new_width * aspect_ratio)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        base_dir = os.path.dirname(__file__)
        ascii_dir = os.path.join(base_dir, 'converted')
        os.makedirs(ascii_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        ascii_path = os.path.join(ascii_dir, f"{search_term}_{timestamp}.txt")

        output = ascii_magic.from_image(image)

        with open(ascii_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"ASCII art saved to: {ascii_path}")
        return output
    except Exception as e:
        honeybadger.notify(e, context={'image_path': image_path, 'search_term': search_term})
        print(f"Error converting to ASCII: {type(e).__name__}: {e}")
        return None


def get_bing_image(search_term, api_key, is_logo=False):
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    if is_logo:
        search_term = f"{search_term} logo transparent"
        params = {
            "q": search_term,
            "license": "public",
            "imageType": "Transparent",
            "count": 5,
            "safeSearch": "Strict",
            "aspect": "Square",
            "minHeight": 200,
            "minWidth": 200
        }
    else:
        params = {
            "q": search_term,
            "license": "public",
            "imageType": "photo",
            "count": 5,
            "safeSearch": "Strict"
        }

    try:
        response = requests.get("https://api.bing.microsoft.com/v7.0/images/search", headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        if "value" not in search_results or not search_results["value"]:
            raise ValueError(f"No image results found for '{search_term}'")

        for image in search_results["value"]:
            try:
                url = image["contentUrl"]
                test_response = requests.head(url, headers=headers, timeout=5)
                if test_response.status_code == 200:
                    return url
            except:
                continue
        raise ValueError("Could not find any accessible images")

    except Exception as e:
        honeybadger.notify(e, context={"search_term": search_term, "is_logo": is_logo})
        raise


def get_duckduckgo_image(search_term, is_logo=False):
    try:
        if is_logo:
            search_term = f"{search_term} logo transparent"

        ddgs = DDGS()
        results = list(ddgs.images(search_term, max_results=5))

        if not results:
            raise ValueError(f"No image results found for '{search_term}'")

        for result in results:
            try:
                url = result["image"]
                test_response = requests.head(url, timeout=5)
                if test_response.status_code == 200:
                    return url
            except:
                continue
        raise ValueError("Could not find any accessible images")
    except Exception as e:
        honeybadger.notify(e, context={"search_term": search_term, "is_logo": is_logo})
        raise

def calculate_cost(search_engine, search_type):
    if search_engine == '1':
        cost_per_transaction = 5 / 1000
        if search_type == '1':
            return cost_per_transaction
        elif search_type == '2':
            return cost_per_transaction * 1.5
    else:
        return 0


def main():
    if not check_honeybadger_connection():
        print("Honeybadger connection failed. Exiting...")
        return

    search_term = input("Enter search term: ")
    search_engine = get_search_engine()
    search_type = get_search_type()

    image_url = search_image(search_term, search_engine, search_type)
    if image_url:
        image_path, temp_image_path = download_image(image_url, search_term)
        if image_path and temp_image_path: #make sure image_path and temp_image_path are good
            ascii_art = convert_to_ascii(image_path, temp_image_path, search_term)
            if ascii_art:
                print(f"\nASCII art for '{search_term}':\n{ascii_art}")
                cost = calculate_cost(search_engine, search_type)
                print(f"\nEstimated cost of this search: ${cost:.4f}")
            try:
                os.remove(temp_image_path) # remove the temp image file
            except Exception as e:
                print(f"Error removing temporary file: {e}")

if __name__ == "__main__":
    main()