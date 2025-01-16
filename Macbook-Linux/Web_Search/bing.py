#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import requests

def bing_web_search(query, api_key):
    endpoint = "https://api.bing.microsoft.com/v7.0/search"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    params = {
        "q": query,
        "count": 10,  # Number of results
        "offset": 0,  # Starting offset
        "mkt": "en-US"  # Market
    }
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        search_results = response.json()
        
        # Process and print search results
        for result in search_results.get('webPages', {}).get('value', []):
            print(f"Title: {result['name']}")
            print(f"URL: {result['url']}")
            print(f"Snippet: {result['snippet']}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"Error performing search: {e}")

# Example usage
api_key = "BING_API_KEY"  # Replace with your actual Bing API key
search_query = "Python programming"
bing_web_search(search_query, api_key)