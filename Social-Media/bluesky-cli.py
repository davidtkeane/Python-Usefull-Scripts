#!/usr/bin/env python3

# Created by Ranger (Dec 2024)
# Version 2.0.0

import os
import time
from dotenv import load_dotenv
from atproto import Client, models
from datetime import datetime
from functools import lru_cache

# pip install atproto 

# Load environment variables
load_dotenv()

# List of available accounts and their configuration files
ACCOUNTS = [
    {"name": "User_1", "identifier": os.getenv("BLUESKY_IDENTIFIER"), "password": os.getenv("BLUESKY_PASSWORD")},

    # Add more accounts as needed, e.g. 
    # To use a 2nd account remove the '#' from the line below and add the necessary environment variables

    # {"name": "user_2", "identifier": os.getenv("SECONDARY_BLUESKY_IDENTIFIER"), "password": os.getenv("SECONDARY_BLUESKY_PASSWORD")}
]

def load_account(choice):
    if choice < 1 or choice >= len(ACCOUNTS):
        print(f"Invalid account choice: {choice}")
        return None
    return ACCOUNTS[choice - 1]

def get_client(account):
    client = Client()
    try:
        client.login(account["identifier"], account["password"])
    except Exception as e:
        print(f"Error logging in to account '{account['name']}': {e}")
        exit(1)
    return client

def main():
    RATE_LIMIT_DELAY = 2  # Add a delay between API calls to respect rate limits

    global current_account
    current_account = None
    
    while True:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting delay
        
        options = """
Options:
1. Send a tweet (primary account)
2. Check new tweets (primary account)
3. See all tweets (with pagination) (primary account)
4. View an author (primary account)
5. Search posts or hashtags (primary account)
6. Check notifications (primary account)
7. View custom timelines/lists (primary account)
8. Switch accounts
9. Exit
"""
        
        print(options)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1' and current_account != ACCOUNTS[0]:
            send_tweet_with_choice()
        elif choice == '2' and current_account != ACCOUNTS[0]:
            check_new_tweets_with_choice()
        elif choice == '3' and current_account != ACCOUNTS[0]:
            see_all_tweets_with_choice()
        elif choice == '4' and current_account != ACCOUNTS[0]:
            view_author_with_choice()
        elif choice == '5' and current_account != ACCOUNTS[0]:
            search_functionality_with_choice()
        elif choice == '6' and current_account != ACCOUNTS[0]:
            check_notifications_with_choice()
        elif choice == '7' and current_account != ACCOUNTS[0]:
            custom_timelines_with_choice()
        
        elif choice == '1':
            send_tweet()
        elif choice == '2':
            check_new_tweets()
        elif choice == '3':
            see_all_tweets()
        elif choice == '4':
            view_author()
        elif choice == '5':
            search_functionality()
        elif choice == '6':
            check_notifications()
        elif choice == '7':
            custom_timelines()
        
        elif choice == '8':
            select_account()
        
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def send_tweet_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    text = input("Enter your tweet: ")
    client = get_client(current_account)
    try:
        post = client.send_post(text)
        print(f"BlueSky Tweet sent successfully! URI: {post.uri}")
    except Exception as e:
        print(f"Error sending tweet: {e}")

def check_new_tweets_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    client = get_client(current_account)
    try:
        timeline = client.get_timeline(limit=10)
        if not timeline.feed:
            print("No new tweets available.")
            return
        print("Latest 10 tweets:")
        for post in timeline.feed:
            print(f"{post.post.author.handle}: {post.post.record.text}")
    except Exception as e:
        print(f"Error fetching new tweets: {e}")

def see_all_tweets_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    client = get_client(current_account)
    try:
        cursor = None
        while True:
            timeline = client.get_timeline(limit=10, cursor=cursor)
            if not timeline.feed:
                print("No more tweets available.")
                break
            for post in timeline.feed:
                print(f"{post.post.author.handle}: {post.post.record.text}")
            cursor = timeline.cursor
            next_page = input("Load more tweets? (y/n): ").lower()
            if next_page != 'y':
                break
    except Exception as e:
        print(f"Error fetching all tweets: {e}")

def view_author_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    author = input("Enter author's handle: ")
    client = get_client(current_account)
    try:
        profile = client.get_profile(author)
        posts = client.get_author_feed(author, limit=10)
        print(f"\nProfile: {profile.display_name} (@{profile.handle})")
        print(f"Description: {profile.description}")
        print("\nLatest 10 posts:")
        for post in posts.feed:
            print(f"- {post.post.record.text}")
    except Exception as e:
        print(f"Error fetching author info: {e}")

def search_functionality_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    query = input("Enter a search term or hashtag (e.g., #example): ")
    client = get_client(current_account)
    try:
        results = client.search_posts(query=query, limit=10)
        for post in results.feed:
            print(f"{post.post.author.handle}: {post.post.record.text}")
    except Exception as e:
        print(f"Error searching posts: {e}")

def check_notifications_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    client = get_client(current_account)
    try:
        notifications = client.get_notifications(limit=10)
        if not notifications.notifications:
            print("No new notifications.")
            return
        for notification in notifications.notifications:
            print(f"{notification.author.handle}: {notification.reason}")
    except Exception as e:
        print(f"Error fetching notifications: {e}")

def custom_timelines_with_choice():
    global current_account
    if not current_account:
        print("No account selected.")
        return
    
    client = get_client(current_account)
    try:
        lists = client.get_lists()
        if not lists.lists:
            print("No custom timelines available.")
            return
        for i, lst in enumerate(lists.lists):
            print(f"{i + 1}. {lst.name}")
        
        choice = int(input("Select a timeline by number: ")) - 1
        if choice < 0 or choice >= len(lists.lists):
            print("Invalid choice.")
            return
        
        selected_list = lists.lists[choice]
        posts = client.get_list_feed(selected_list.uri, limit=10)
        
        for post in posts.feed:
            print(f"{post.post.author.handle}: {post.post.record.text}")
    except Exception as e:
        print(f"Error fetching custom timelines: {e}")

def select_account():
    global current_account
    
    if not current_account:
        print("No account selected. Select an account by number:")
    
    for i, account in enumerate(ACCOUNTS):
        print(f"{i + 1}. {account['name']}")
    
    choice = input("Enter your choice: ")
    
    try:
        choice = int(choice) - 1
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return
    
    current_account = ACCOUNTS[choice]

def main_with_choice():
    RATE_LIMIT_DELAY = 2  # Add a delay between API calls to respect rate limits

    global current_account
    current_account = None
    
    while True:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting delay
        
        options = """
Options for {account['name']}:
1. Send a tweet
2. Check new tweets
3. See all tweets (with pagination)
4. View an author
5. Search posts or hashtags
6. Check notifications
7. View custom timelines/lists
8. Switch accounts
9. Exit
""".format(account=current_account if current_account else ACCOUNTS[0])
        
        print(options)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            send_tweet()
        elif choice == '2':
            check_new_tweets()
        elif choice == '3':
            see_all_tweets()
        elif choice == '4':
            view_author()
        elif choice == '5':
            search_functionality()
        elif choice == '6':
            check_notifications()
        elif choice == '7':
            custom_timelines()
        
        elif choice == '8':
            select_account()
        
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()