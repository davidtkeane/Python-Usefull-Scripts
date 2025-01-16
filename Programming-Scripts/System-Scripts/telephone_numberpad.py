#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

from itertools import product

# Phone number mapping
mapping = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': '0',
    '1': '1'
}

# List of phone numbers from your input
phone_numbers = [
    "+35319128183",
    "+35319640427",
    "+35319640296",
    "+35319128455",
    "+35319640956",
    "+35319128045",
    "+35319128987",
    "+35319128013",
    "+35319640987",
    "+35319128396",
    "+35319640952",
    "+35319128124",
    "+35319640958",
    "+35319128168",
    "+35319128450",
    "+35319640083",
    "+35319640942",
    "+35319128491",
    "+35319128835",
    "+35319640089",
    "+35319128515",
    "+35319640076",
    "+35319640999",
    "+35319640324",
    "+35319640424",
    "+35319640921",
    "+35319128905",
    "+35319128405",
    "+35319640934",
    "+35319128139"
]

# Function to generate letter combinations for a phone number
def generate_combinations(number):
    letters = [mapping[digit] for digit in number if digit in mapping]
    return [''.join(combo) for combo in product(*letters)]

# Iterate through the phone numbers and generate combinations
for number in phone_numbers:
    local_number = number[-11:]  # Extract the last 7 digits
    combinations = generate_combinations(local_number)
    print(f"Combinations for {number}: {combinations}")  # Print all combinations

print("Script executed successfully.")