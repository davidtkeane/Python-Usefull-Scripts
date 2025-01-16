#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# This script provides a simple example of how to use the Flask web framework to create a basic web application.

# Import necessary libraries
# --- Imports ---
from flask import Flask # Import Flask from flask module

app = Flask(__name__) # Create an instance of Flask class for our web app 

@app.route("/") # Define the URL for the default route of web application
def index(): # Define a function to return a string when the default route is accessed
    return "Ranger says hi" # Return a string to be displayed on the web page

app.run(host="0.0.0.0", port=80) # Run the Flask web server with the specified host and port
