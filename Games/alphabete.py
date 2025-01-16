#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name: Multilingual Alphabet Bar
# Created by Ranger (Dec 2024) 😎
# Version: 2.1.0
#
# Description:
# A simple tkinter application that displays a bar of characters for several languages, including ancient ones.
# It can be used to quickly copy characters to clipboard and have a better visual reference
# for different alphabets.

import tkinter as tk
from typing import List, Tuple
from tkinter import ttk
from PIL import Image, ImageTk  # Import Pillow library


# --- Data Definitions ---

# Color and character definitions for different alphabets
ALPHABET_INFO = {
    "Numbers": ("#FF5733", range(1, 34)),  # Color Red-Orange
    "Eng": ("#FF4500", (chr(65 + i) for i in range(26))),  # Color Red
    "Eng2": ("#808080", "abcdefghijklmnopqrstuvwxyz"),  # Color Gray
    "French": ("#FF1493", "ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝ"),  # Color Pink
    "Roman": ("#FF4500", ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII"]),  # Color Red
    "Hebrew": ("#8A2BE2", "אבגדהוזחטיכלמנסעפצקרשת"),  # Color Blue-Violet
    "Greek": ("#808080", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"),  # Color Gray
    "Russian": ("#FF69B4", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),  # Color Hot Pink
    "Ukrainian": ("#ADD8E6", "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"), # Color Red-Orange
    "Japanese": ("#FF5733", "あいうえお かきくけこ さしすせそ たちつてと なにぬねの はひふへほ まみむめもら わんねんわんにわんえんわんいわんうわんお"),
    "Chinese": ("#FF0000", "一二三四五六七八九十百千万 甲乙丙丁戊己庚辛壬癸 子丑寅卯辰巳午未申酉戌亥"), # Color Red
    "Korean": ("#4CAF50", "가나다라마바사아자차카타파하 ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"),  # Color Green
    "Spanish": ("#FFD700", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"),  # Color Yellow
    "German": ("#00CED1", "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"),    # Color Dark Turquoise
    "Italian": ("#FFA07A", "ABCDEFGHIJKLMNOQRSTUVWYZ"), # Color Salmon
    "Norwegian": ("#98FB98", "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"), # Color Pale Green
    "Arabic": ("#FF4500", "أبتثجحخدذرزسشصضطظعغفقكلمنهوي"),  # Color Red
    "Aramaic": ("#FF0000", "ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ"),  # Color Red
    "Persian": ("#FFC125", "۰۱۲۳۴۵۶۷۸۹۰"),  # Color Amber
    # Color Red - Hieroglyphs need to have the font installed, so this will
    # most likely print squares.
    "Hieroglyphic": ("#FF0000", "𓀀𓀁𓀂𓀃𓀄𓀅𓀆𓀇𓀈𓀉𓀊𓀋𓀌𓀍𓀎𓀏𓀐𓀑𓀒𓀓𓀔𓀕𓀖𓀗𓀘𓀙𓀚𓀛𓀜𓀝𓀞𓀟𓀠𓀡𓀢𓀣𓀤𓀥𓀦𓀧𓀨𓀩𓀪𓀫𓀬𓀭𓀮𓀯𓀰𓀱𓀲𓀳𓀴𓀵𓀶𓀷𓀸𓀹𓀺𓀻𓀼𓀽𓀾𓀿"), # Color Red
    "Cyrillic": ("#FF0000", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
    "Greek": ("#FF0000", "αβγδεζηθικλμνοπρστυφχψωέία"),  # Color Red
    "Turkish": ("#FF0000", "abcçdeöğhıijklmnpqrstvwxyz"),  # Color Red
    "Spanish": ("#FF0000", "áéíóúüñ"),  # Color Red
    "French": ("#FF0000", "àâçéêîôùü"),  # Color Red
    "Old Italic": ("#FF0000", "𐌀𐌁𐌂𐌃𐌄𐌅𐌆𐌇𐌈𐌉𐌊𐌋𐌌𐌍𐌎𐌏𐌐𐌑𐌒𐌓𐌔𐌕𐌖𐌗𐌘𐌙𐌚"),  # Color Red
    "Coptic": ("#FF0000", "ϠϡϢϣϤϥϦϧϨϩ"),  # Color Red
    "Phoenician": ("#FF0000", "𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋"),  # Color Red
    "Roman": ("#FF0000", "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX"), # Color Red
    "Runic": ("#FF0000", "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛟᛞᛖ"),  # Color Red
    "Ogham": ("#FF0000", "ᚁᚂᚃᚄᚅᚆᚇᚈᚉᚍᚌᚏᚙᚐᚑᚘᚔᚚ᚛"),  # Color Red
}

# Emoji associated with each alphabet origin
ALPHABET_EMOJIS = {
    "Numbers": "🔢",
    "Eng": "🇬🇧",
    "Eng2": "🇬🇧",
    "French": "🇫🇷",
    "Roman": "🏛️",
    "Hebrew": "🇮🇱",
    "Greek": "🇬🇷",
    "Russian": "🇷🇺",
    "Ukrainian": "🇺🇦",
    "Japanese": "🇯🇵",
    "Chinese": "🇨🇳",
    "Korean": "🇰🇷",
    "Thai": "🇹🇭",
    "Indonesian": "🇮🇩",
    "Arabic": "🇸🇦",
    "Dutch": "🇳🇱",
    "Portuguese": "🇵🇹",
    "Spanish": "🇪🇸",
    "German": "🇩🇪",
    "Italian": "🇮🇹",
    "Norwegian": "🇳🇴",
    "Aramaic": "🇮🇶",
    "Persian": "🇮🇷",
    "Hieroglyphic": "🇪🇬",
    "Old Italic": "🇮🇹",
    "Runic": "ᚠ",
    "Ogham": "🇮🇪",
    "Cyrillic": "🇷🇺"
}


# --- Functions ---

def create_alphabet_bar():
    """Creates the main window and populates the alphabet bar."""
    window = tk.Tk()
    window.title("Multilingual Alphabet Bar")
    window.geometry("900x600")  # Set initial size
    window.resizable(False, False)  # Disable resizing
    

    # Custom Title Bar
    title_bar = tk.Frame(window, bg="gray", relief="raised", bd=2)
    title_bar.pack(fill=tk.X)
    title_label = tk.Label(title_bar, text="Made by Ranger", bg="gray")
    title_label.pack(side=tk.LEFT, padx=10)

    # Make the window stay on top and remove title bar
    window.attributes("-topmost", True)

    # Frame to hold the content
    frame = tk.Frame(window)
    frame.pack(expand=True, fill=tk.BOTH)

    for country, (color, characters) in ALPHABET_INFO.items():
        # Default emoji for unknown origin
        flag_emoji = ALPHABET_EMOJIS.get(country, "🌐")
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
    """Helper function to add a row of characters to the frame."""
    row = len(frame.grid_slaves()) // 26
    tk.Label(frame, text=country, fg=color).grid(row=row, column=1)
    for i, char in enumerate(characters):
        tk.Label(frame, text=char, fg=color).grid(row=row, column=i + 2)


# --- Main Script Execution ---
if __name__ == "__main__":
    create_alphabet_bar()
