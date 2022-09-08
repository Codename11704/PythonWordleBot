from msilib.schema import Icon
import pygame
import array


WORDSBUFFER = []
WORDS = []

ANSWERSBUFFER = []
ANSWERS = []

def init():
    global ICON, FONT
    FONT = pygame.font.Font('me/sean/pywordlebot/assets/arial.ttf', 32)
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
