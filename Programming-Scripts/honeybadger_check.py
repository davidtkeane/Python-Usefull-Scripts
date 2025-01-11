#!/Users/ranger/.pyenv/shims/python3 # <-- This is my shebang actual path. Check with "which python" in terminal, then replace.
# -*- coding: utf-8 -*-

# Created by Ranger

# honeybadger

from flask import Flask, jsonify, request
from honeybadger.contrib import FlaskHoneybadger

app = Flask(__name__)
app.config['HONEYBADGER_ENVIRONMENT'] = 'notifications'
app.config['HONEYBADGER_API_KEY'] = 'Enter API KEY HERE'
app.config['HONEYBADGER_PARAMS_FILTERS'] = 'password, secret, credit-card'
FlaskHoneybadger(app, report_exceptions=True)

@app.route('/')
def index():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    print('Dividing two numbers {} {}'.format(a, b))
    return jsonify({'result': a / b})

[...]

from honeybadger import honeybadger
honeybadger.configure(api_key='hbp_i1dvSEEHvv1kDXsZoomGrkSamt1ida24sihc')

raise Exception("This will get reported!")