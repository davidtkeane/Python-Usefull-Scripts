#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import tkinter as tk
from PIL import Image, ImageTk

# Function to create the alphabet bar
def create_alphabet_bar():
    window = tk.Tk()
    window.title("Multilingual Alphabet Bar")

    # Colors for different alphabets
    alphabet_info = {
        "Numbers": ("#FF5733", range(1, 34)),
        "Eng": ("#FF4500", (chr(65 + i) for i in range(26))),
        "Eng2": ("#808080", "abcdefghijklmnopqrstuvwxyz"),
        "French": ("#FF1493", "ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝ"),
        "Roman": ("#FF4500", ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII"]),
        "Hebrew": ("#8A2BE2", "אבגדהוזחטיכלמנסעפצקרשת"),
        "Greek": ("#808080", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"),
        "Russian": ("#FF69B4", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
        "Spanish": ("#FFD700", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"),
        "German": ("#00CED1", "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"),
        "Italian": ("#FFA07A", "ABCDEFGHIJKLMNOQRSTUVWYZ"),
        "Norwegian": ("#98FB98", "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"),
        "Ukrainian": ("#ADD8E6", "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ")
    }

    alphabet_emojis = {
        "Numbers": "🔢",
        "Eng": "🇬🇧",
        "Eng2": "🇬🇧",        
        "French": "🇫🇷",
        "Roman": "🏛️",
        "Hebrew": "🇮🇱",
        "Greek": "🇬🇷",
        "Russian": "🇷🇺",
        "Spanish": "🇪🇸",
        "German": "🇩🇪",
        "Italian": "🇮🇹",
        "Norwegian": "🇳🇴",
        "Ukrainian": "🇺🇦"
    }

    # Custom Title Bar
    title_bar = tk.Frame(window, bg="gray", relief="raised", bd=2)
    title_bar.pack(fill=tk.X)
    title_label = tk.Label(title_bar, text="Made by Ranger", bg="gray")
    title_label.pack(side=tk.LEFT, padx=10)

    # Close Button
    close_button = tk.Button(title_bar, command=window.destroy, bg="gray")
    # close_button.pack(side=tk.RIGHT)

    # Make the window stay on top and remove title bar
    window.attributes("-topmost", True)

    # Frame to hold the content
    frame = tk.Frame(window)
    frame.pack(expand=True, fill=tk.BOTH)

    for country, (color, characters) in alphabet_info.items():
        flag_emoji = alphabet_emojis.get(country, "🌐")  # Default emoji for unknown origin
        flag_label = tk.Label(frame, text=flag_emoji, fg=color)
        flag_label.grid(row=0, column=0, sticky="w")

        add_alphabet(frame, characters, color, country)

    # Function to enable window drag
    def on_drag(event):
        window.geometry(f"+{event.x_root}+{event.y_root}")

    # Bind mouse movement to the function
    title_bar.bind("<B1-Motion>", on_drag)

    window.mainloop()

def add_alphabet(frame, characters, color, country):
    """ Helper function to add a row of characters to the frame """
    row = len(frame.grid_slaves()) // 26
    tk.Label(frame, text=country, fg=color).grid(row=row, column=1)
    for i, char in enumerate(characters):
        tk.Label(frame, text=char, fg=color).grid(row=row, column=i + 2)

create_alphabet_bar()
