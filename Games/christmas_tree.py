#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---
import argparse
import os
import random
import time
from PIL import Image

BALL = '⏺'
COLOR = {
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}
STAR = '★'

def random_change_char(string, value):
    indexes = random.sample(range(0, len(string)), value)
    string = list(string)
    for idx in indexes:
        if string[idx] != ' ' and string[idx] == '_':
            string[idx] = BALL
    return ''.join(string)

def tree(height=13, screen_width=80):
    star = (STAR, 3*STAR)
    if height % 2 != 0:
        height += 1
    body = ['/_\\', '/_\_\\']
    trunk = '[___]'
    begin = '/'
    end = '\\'
    pattern = '_/'
    j = 5
    for i in range(7, height + 1, 2):
        middle = pattern + (i - j) * pattern
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        middle = middle.replace('/', '\\')
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        j += 1

    return [line.center(screen_width) for line in (*star, *body, trunk)]

def balls(tree):
    for idx, _ in enumerate(tree[:-3], 2):
        tree[idx] = random_change_char(tree[idx], len(tree[idx])//8)
    return tree

def colored_stars_balls(tree):
    for idx, _ in enumerate(tree):
        string = list(tree[idx])
        for pos, _ in enumerate(string):
            if string[pos] == STAR:
                string[pos] = ''.join([COLOR['yellow'], STAR, '\033[0m'])
            elif string[pos] == BALL:
                string[pos] = ''.join([random.choice(list(COLOR.values())), BALL, '\033[0m'])
        tree[idx] = ''.join(string)
    return tree

def load_gif_frames(gif_path):
    """
    Loads frames of a GIF into a list of images.

    Args:
        gif_path (str): Path to the GIF file.

    Returns:
        list: List of Image objects representing GIF frames.
    """
    try:
        gif = Image.open(gif_path)
        frames = []
        try:
            while True:
                frames.append(gif.copy())
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass  # End of GIF
        return frames
    except Exception as e:
        print(f"Error loading GIF '{gif_path}': {e}")
        return None

def display_gif_frame(frame):
    """
    Displays a single frame of a GIF as text.
    """
    try:
        width, height = os.get_terminal_size()
        resized_frame = frame.resize((width, height), Image.NEAREST)

        text_frame = ""
        for y in range(resized_frame.height):
          line = ""
          for x in range(resized_frame.width):
            pixel = resized_frame.getpixel((x,y))
            # Convert pixel to grayscale value (0-255)
            grayscale = int((pixel[0] * 0.299 + pixel[1] * 0.587 + pixel[2] * 0.114) / 255 * 10)

            # Map grayscale to characters for text representation
            chars = " .:-=+*#%@"
            char_index = min(grayscale, len(chars)-1) # Make sure it is not out of bounds
            line += chars[char_index]
          text_frame += line + "\n"
        return text_frame
    except Exception as e:
        print(f"Error displaying GIF frame: {e}")
        return ""


def cli():
    parser = argparse.ArgumentParser(prog="Python Christmas Tree by Chico Lucio from Ciencia Programada",
                                     epilog="Ctrl-C interrupts the Christmas :-(")
    parser.add_argument('-s', '--size', default=13, type=int,
                        help="Tree height. If even it will be subtracted 1. If less than 7, considered 5. Default: 13")
    parser.add_argument('-w', '--width', default=80, type=int,
                        help="Screen width. Used to center the tree. Default: 80")
    parser.add_argument('-t', '--terminal', action='store_true',
                        help="Uses the terminal size to center the tree. -s and -w will be ignored")
    parser.add_argument('-g', '--gif-mode', default='none', choices=['none', 'both', 'single'],
                        help="GIF mode: 'none' to disable, 'single' to use the first, 'both' to alternate between the two. Default: none")
    parser.add_argument('-gs', '--gif-speed', type=float, default=0.1,
                        help="Speed of GIF frame switching. Default 0.1")
    args = parser.parse_args()

    if args.terminal:
        screen_width, height = os.get_terminal_size()
        height -= 2
    else:
        height = args.size
        screen_width = args.width

    # Load GIF frames
    gif_frames = []
    reversed_gif_frames = []
    if args.gif_mode != 'none':
        gif_frames = load_gif_frames('tree.gif')
        if args.gif_mode == 'both':
            reversed_gif_frames = load_gif_frames('tree_reversed.gif')

        if not gif_frames:
            args.gif_mode = 'none' # Disable GIF mode
        elif args.gif_mode == 'both' and not reversed_gif_frames:
            args.gif_mode = 'single' # Switch to single gif mode if the other is missing.


    gif_index = 0
    reversed_gif_index = 0
    use_reversed = False

    while True:
        try:
            time.sleep(random.uniform(0.1, 1))
            os.system('cls' if os.name == 'nt' else 'clear')

            if args.gif_mode == 'none':
               print('\n'.join(colored_stars_balls(balls(tree(height, screen_width)))))
            elif args.gif_mode == 'single':
                frame = gif_frames[gif_index % len(gif_frames)]
                print(display_gif_frame(frame))
                time.sleep(args.gif_speed)
                gif_index += 1
            elif args.gif_mode == 'both':
                if use_reversed:
                    frame = reversed_gif_frames[reversed_gif_index % len(reversed_gif_frames)]
                    reversed_gif_index += 1
                else:
                    frame = gif_frames[gif_index % len(gif_frames)]
                    gif_index += 1
                print(display_gif_frame(frame))
                time.sleep(args.gif_speed)
                use_reversed = not use_reversed

        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{'Merry Christmas!!':^{screen_width}}", end='\n\n')
            break

if __name__ == '__main__':
    cli() 