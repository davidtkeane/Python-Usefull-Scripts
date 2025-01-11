#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import random

# List of motivational quotes
quotes = ["The only limit to our realization of tomorrow will be our doubts of today.",
          "It does not matter how slowly you go as long as you do not stop.",
          "Success is not final, failure is not fatal: It is the courage to continue that counts.",
          "The journey of a thousand miles begins with a single step.",
          "Believe you can and you're halfway there.",
          "The only way to do great work is to love what you do.",
          "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful."]

# ASCII art design
design = '''
    *\n
   /**\n
  /****\n
 /******\n
/**********/\n
\**********\\n
 \**********\\\n
  \**********\\\n
   \**********\\\n
    \**********\\\n
    /*    \**********\/\n
   /       \**********\/\n
  /          \**********\/\n
 /             \**********\/\n
/                \**********\/\n
'''

# Function to randomly select a quote
def generate_quote():
    quote = random.choice(quotes)
    return quote

# Display the quote with the ASCII art design
print(design)
print(generate_quote())

