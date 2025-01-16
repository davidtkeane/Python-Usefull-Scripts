#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

import turtle

t = turtle.Turtle()
t.shapesize(0.2, 0.2)
s = turtle.Screen()
s.bgcolor ('black')

t.speed (5)
t.fillcolor ("yellow")
t.begin_fill()

t.left (50)
t.forward (240)
t.circle(90, 200)
t.left (221)
t.circle (90, 200)
t.forward (260)

t.end_fill()

turtle.done()

# cLcoding.com (2021) How to Create a Yellow Heart Using Turtle in Python. https://clcoding.com/python/how-to-create-a-yellow-heart-using-turtle-in-python/ (Accessed on 2024-07-16)

# The code above is a simple code that creates a yellow heart using the turtle module in Python. 
# The code creates a turtle object and sets the shape size to 0.2, 0.2. 
# The screen background color is set to black, and the turtle fill color is set to yellow. 
# The turtle then begins filling the shape and draws the heart using the forward and circle functions. 
# The heart is then filled with the yellow color, and the turtle.done() function is called to keep the window open. 
# The code creates a simple yellow heart shape using the turtle module in Python. (Clcoding.com, 2021)