#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

import turtle
import random

wn=turtle.Screen()
wn.setup(600,600)
#wn.bgcolor(red) 
s=turtle.Turtle()

r=10
for i in range(200):
    s.circle(r+i,45)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))
s.penup()
s.home()
s.pendown()

m=20
for i in range(200):
    s.circle(m+i,45)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))
s.penup()
s.home()
s.pendown()

n=30
for i in range(200):
    s.circle(n+i,45)
    j=random.random()
    k=random.random()
    l=random.random()
    s.pencolor((j,k,l))    

turtle.done()