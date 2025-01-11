#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# Import necessary libraries
# --- Imports ---

# Quiz Game
print ("Welcome to my new game!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()
    
print ("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer =="Central Processing Unit":
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')
    
answer = input("What does PSY stand for? ").lower()
if answer =="psychology":
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer!')
    
answer = input("What is pi? ")
if answer =="3.14":
    print('Correct answer Einstien!')
    score += 1
else:
    print('Wrong answer!')
    
answer = input("How many planets are there in the solar system? ")
if answer =="9":
    print("NEIN!!!!!!")
    score += 1
else:
    print('Wrong answer!')
    
print("You got " + str(score) +  " of the question correct!")
print("You got " + str((score / 4) * 100) + "%. " " of the question correct!")