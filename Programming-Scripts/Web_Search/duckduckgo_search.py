#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import requests

def duckduckgo_search(query):
    # DuckDuckGo API endpoint
    url = "https://api.duckduckgo.com/"
    
    # Parameters for the API request
    params = {
        "q": query,          # Search query
        "format": "json",    # Response format (JSON)
        "no_html": 1,        # Exclude HTML from the response
        "skip_disambig": 1   # Skip disambiguation pages
    }
    
    try:
        # Send GET request to DuckDuckGo API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Display the results
        print(f"Search Results for: {query}\n")
        print(f"Abstract: {data.get('AbstractText', 'No abstract available')}\n")
        print(f"URL: {data.get('AbstractURL', 'No URL available')}\n")
        
        if data.get('RelatedTopics'):
            print("Related Topics:")
            for topic in data['RelatedTopics']:
                print(f"- {topic.get('Text', 'No text available')}")
        else:
            print("No related topics found.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    duckduckgo_search(search_query)