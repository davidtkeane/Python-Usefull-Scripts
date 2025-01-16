#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_folder():
    folder_path.set(filedialog.askdirectory())

def select_files():
    file_paths.set(filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png")]))

def select_output_folder():
    output_folder_path.set(filedialog.askdirectory())

def convert_to_webp():
    if folder_path.get():
        for file_name in os.listdir(folder_path.get()):
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                img = Image.open(os.path.join(folder_path.get(), file_name))
                img.save(os.path.join(output_folder_path.get(), os.path.splitext(file_name)[0] + '.webp'), 'webp')
    if file_paths.get():
        for file_path in root.tk.splitlist(file_paths.get()):
            img = Image.open(file_path)
            img.save(os.path.join(output_folder_path.get(), os.path.splitext(os.path.basename(file_path))[0] + '.webp'), 'webp')
    messagebox.showinfo("Information","Conversion complete")

root = tk.Tk()

folder_path = tk.StringVar()
file_paths = tk.StringVar()
output_folder_path = tk.StringVar()

tk.Label(root, text="Select folder:").grid(row=0, column=0)
tk.Entry(root, textvariable=folder_path).grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_folder).grid(row=0, column=2)

tk.Label(root, text="Select file(s):").grid(row=1, column=0)
tk.Entry(root, textvariable=file_paths).grid(row=1, column=1)
tk.Button(root, text="Browse", command=select_files).grid(row=1, column=2)

tk.Button(root, text="Convert to WebP", command=convert_to_webp).grid(row=2, column=1)

tk.Label(root, text="Select output folder:").grid(row=3, column=0)
tk.Entry(root, textvariable=output_folder_path).grid(row=3, column=1)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=3, column=2)

root.mainloop()
