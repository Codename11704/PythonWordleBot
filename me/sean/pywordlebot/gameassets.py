"""
Author: Sean Droll
Date: 9/10/22

This file initializes all the assets for the wordle game
"""

import pygame
import random


WORDSBUFFER = []
WORDS = []

ANSWERSBUFFER = []
ANSWERS = []


def chooseWord():
    """
    This function chooses a random word from a file of possible wordle solutions,
    this word will be the word the user tries to guess
    """
    size = ANSWERS.__len__()
    ind = random.randrange(0, size)
    word = ANSWERS[ind]
    return word


def init():
    """
    Initializes all the assets used for wordle
    """
    global ICON, LETTERFONT, MESSAGEFONT, WORDLEWORD
    LETTERFONT = pygame.font.Font('me/sean/pywordlebot/assets/arial.ttf', 32)
    MESSAGEFONT = pygame.font.Font('me/sean/pywordlebot/assets/arial.ttf', 16)
    ICON = pygame.image.load("me/sean/pywordlebot/assets/logo.png")

    with open("me/sean/pywordlebot/assets/valid-wordle-words.txt") as f:
        WORDSBUFFER = f.readlines()
        
        for word in WORDSBUFFER:
            s = word.strip('\n')
            WORDS.append(s.upper())
            
    
    with open("me/sean/pywordlebot/assets/valid-wordle-solutions.txt") as f:
        ANSWERSBUFFER = f.readlines()

        for word in ANSWERSBUFFER:
            s = word.strip('\n')
            ANSWERS.append(s.upper())
    WORDLEWORD = chooseWord()
    
