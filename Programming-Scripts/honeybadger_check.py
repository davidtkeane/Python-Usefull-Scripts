#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Usage: python honeybadger_check.py

# Import necessary libraries
# --- Imports ---
from flask import Flask, jsonify, request
from honeybadger.contrib import FlaskHoneybadger

# Initialize Flask app
app = Flask(__name__)
app.config['HONEYBADGER_ENVIRONMENT'] = 'Your Project Environment Name'
app.config['HONEYBADGER_API_KEY'] = 'Enter API KEY HERE'
app.config['HONEYBADGER_PARAMS_FILTERS'] = 'password, secret, credit-card'  # You might want to filter out sensitive data

# Initialize Honeybadger middleware
FlaskHoneybadger(app, report_exceptions=True)

# Define a route that divides two numbers
@app.route('/')
def index():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    print('Dividing two numbers {} {}'.format(a, b))
    return jsonify({'result': a / b})

[...]

# Run the app
from honeybadger import honeybadger
honeybadger.configure(api_key='Enter APi Key Here')

# This will raise an exception that will be reported to Honeybadger
raise Exception("This will get reported!")