#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# This is a Python script that connects to your Local MongoDB deployment using the PyMongo driver for testing a connection.
# Replace the placeholder values with your own values and run the script using the following command: python mongodb_test.py
# You can get the connection URI from the Connect dialog in the Atlas UI. Make sure to replace myFirstDatabase with the name of the database that connection URI should connect to.
# Type of connection Password (SCRAM) is the type of authentication mechanism used to authenticate the user. For example, SCRAM-SHA-1 or SCRAM-SHA-256.

# Import necessary libraries
# --- Imports ---
# Import the MongoClient class from the pymongo package
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ranger: # Replace this with your own connection URI"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

