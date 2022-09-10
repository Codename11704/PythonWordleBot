"""
Author: Sean Droll
Date: 9/10/2022
This program is a fully functional wordle program
"""
import pygame as pg
import math
import gameassets
import wordchecker as wc

#Window Constants
SIZE = WIDTH, HEIGHT = 600, 700
MAINBLOCKSIZE = math.floor(math.sqrt(HEIGHT*WIDTH*.013))

#Arrays for Colors and such else
GRID = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
ALPHABETQWERTY = list("qwertyuiopasdfghjklzxcvbnm")
ALPHCOLOR = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

#Constants for drawing
ROW = 0
COLUMN = 0

ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (201, 201, 201)
DARKGRAY = (134, 136, 138)
YELLOW = (241, 218, 33)
GREEN = (106, 170, 100)

def drawMainGrid():
    """
    This function draws the main grid used for Wordle
    """
    gridWidth = 5*MAINBLOCKSIZE
    gridHeight = 6*MAINBLOCKSIZE
    xmargin = (WIDTH - gridWidth)//2
    ymargin = math.floor(MAINBLOCKSIZE*(2/3))
    for x in range(xmargin, xmargin + gridWidth, MAINBLOCKSIZE):
        for y in range(ymargin, ymargin + gridHeight, MAINBLOCKSIZE):
            rect = pg.Rect(x, y, MAINBLOCKSIZE, MAINBLOCKSIZE)
            pg.draw.rect(SCREEN, BLACK, rect, 1)


def drawLetterGrid():
    """
    Draws the grid used to show the status of all the letters
    """
    blockSize = math.floor(MAINBLOCKSIZE/1.5)
    y = MAINBLOCKSIZE*6 + 2*blockSize

    gridWidth1 = 10*blockSize
    gridWidth2 = 9*blockSize
    gridWidth3 = 7*blockSize

    xmargin1 = math.floor((WIDTH - gridWidth1)/2)
    xmargin2 = math.floor((WIDTH - gridWidth2)/2)
    xmargin3 = math.floor((WIDTH - gridWidth3)/2)

    counter = 0
    for x in range(xmargin1, xmargin1 + gridWidth1, blockSize):
        color = GRAY
        match ALPHCOLOR[counter]:
            case -1:
                color = GRAY
            case 0:
                color = DARKGRAY
            case 1:
                color = YELLOW
            case 2:
                color = GREEN
            
        rect1 = pg.Rect(x, y, blockSize, blockSize)
        pg.draw.rect(SCREEN, color, rect1)
        rect2 = pg.Rect(x, y, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect2, 1) 
        printLetter(ALPHABETQWERTY[counter], x, y, blockSize, color)
        counter +=1



    for x in range(xmargin2, xmargin2 + gridWidth2, blockSize):
        color = GRAY
        match ALPHCOLOR[counter]:
            case -1:
                color = GRAY
            case 0:
                color = DARKGRAY
            case 1:
                color = YELLOW
            case 2:
                color = GREEN  
        rect1 = pg.Rect(x, y + blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, color, rect1)
        rect2 = pg.Rect(x, y + blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect2, 1) 
        printLetter(ALPHABETQWERTY[counter], x, y + blockSize, blockSize, color)
        counter +=1


    for x in range(xmargin3, xmargin3 + gridWidth3, blockSize):
        color = GRAY
        match ALPHCOLOR[counter]:
            case -1:
                color = GRAY
            case 0:
                color = DARKGRAY
            case 1:
                color = YELLOW
            case 2:
                color = GREEN
            
        rect1 = pg.Rect(x, y + 2*blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, color, rect1)
        rect2 = pg.Rect(x, y + 2*blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect2, 1) 
        printLetter(ALPHABETQWERTY[counter], x, y + 2*blockSize, blockSize, color)
        counter +=1




def printLetter(s, x, y, rectSize, color):
    """
    Prints a letter of a color
    :param s: The letter to be printed
    :param x: The x coordinate of the letter to be printed
    :param y: the y coordinate of the letter to be printed
    :param rectsize: the height and width of the letter to be printed
    :param color: The background color of the letter to be printed
    """
    if s == "":
        rect1 = pg.Rect(x, y, rectSize, rectSize)
        pg.draw.rect(SCREEN, GRAY, rect1)
        rect2 = pg.Rect(x, y, rectSize, rectSize)
        pg.draw.rect(SCREEN, BLACK, rect2, 1)
    else:
        text = gameassets.LETTERFONT.render(s.upper(), True, BLACK, color)
        textRect = text.get_rect()
        textRect.center = (x + rectSize//2, y + rectSize//2)
        SCREEN.blit(text, textRect)


def paintResults(colors, guess):
    """
    Paints the results of the word check
    :param colors: An array that contains the color of each block
    :param guess: the word the user guessed
    """
    gArr = list(guess)
    
    for i in range(0, 5):
        print(i)
        color = GRAY
        match colors[i]:
            case 0:
                color = DARKGRAY
            case 1:
                color = YELLOW
            case 2:
                color = GREEN
        
        text = gameassets.LETTERFONT.render(gArr[i].upper(), True, BLACK, color)
        x = ((WIDTH - 5*MAINBLOCKSIZE)//2) + i*MAINBLOCKSIZE

        rect1 = pg.Rect(x, COLUMNCOORDS, MAINBLOCKSIZE, MAINBLOCKSIZE)
        pg.draw.rect(SCREEN, color, rect1)
        rect2 = pg.Rect(x, COLUMNCOORDS, MAINBLOCKSIZE, MAINBLOCKSIZE)
        pg.draw.rect(SCREEN, BLACK, rect2, 1)


        textRect = text.get_rect()
        textRect.center = (x + MAINBLOCKSIZE//2, COLUMNCOORDS + MAINBLOCKSIZE//2)
        textRect.width = MAINBLOCKSIZE
        textRect.height = MAINBLOCKSIZE
        SCREEN.blit(text, textRect)


def updateGridColors(colors, word):
    """
    Updates the colors in the lower alphabet grid
    :param colors: The colors that resulted from the users guess
    :param word: The users guess
    """
    wordLetters = list(word)
    colorGrid = ALPHCOLOR
    for x in range(0, 5):
        ind = ALPHABETQWERTY.index(wordLetters[x])
        if colorGrid[ind] == 2:
            pass
        else:
            colorGrid[ind] = colors[x]
    return colorGrid

def displayMessage(message):
    """
    Displays a message on the top of the screen and deletes the previous message
    :param message: The message to be displayed
    """
    rect1 = pg.Rect(0, MAINBLOCKSIZE//3-16, WIDTH, 16)
    pg.draw.rect(SCREEN, GRAY, rect1)
    text = gameassets.MESSAGEFONT.render(message, True, BLACK, GRAY)
    textRect = text.get_rect()
    textRect.center = (WIDTH//2, MAINBLOCKSIZE//3-8)
    SCREEN.blit(text, textRect)


def listToString(s):
    """
    Turns a list of characters into a string
    :param s: The character list to be turned into a string
    """
    str1 = ""

    for char in s:
        str1 += char

    return str1

def checkIfValid(s):
    """
    Checks if a given word is a valid wordle answer
    :param s: The word to be checked
    """
    if gameassets.WORDS.__contains__(str(s).upper()):
        return True
    else:
        return False


if __name__ == "__main__":
    #Initialize
    global SCREEN
    pg.init()
    gameassets.init()
    pg.display.set_caption("Wordle Bot")
    pg.display.set_icon(gameassets.ICON)
    SCREEN = pg.display.set_mode(SIZE)
    SCREEN.fill(GRAY)
    drawMainGrid()
    drawLetterGrid()

    #GameLoop
    running = True
    flag = True
    while running:
        #EventQueue
        for event in pg.event.get():
            #EndsGame if either win or lose
            if flag:
                #Runs if key is pressed
                if event.type == pg.KEYDOWN:
                    #checks type of key
                    match event.key:
                        #BackSpace
                        case 8:
                            if ROW == 0:
                                pass
                            else:
                                ROW = ROW - 1
                                GRID[COLUMN][ROW] = ""
                                ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
                                printLetter("", ROWCOORDS, COLUMNCOORDS, MAINBLOCKSIZE, BLACK)
                        #Enter
                        case 13:
                            #Check if row is filled
                            if(ROW == 5):
                                #Checks if valid wordle answer
                                if(checkIfValid(listToString(GRID[COLUMN]))):
                                    wordle = listToString(GRID[COLUMN])
                                    colors = wc.checkWord(gameassets.WORDLEWORD, wordle.upper())
                                    paintResults(colors, wordle)
                                    ALPHCOLOR = updateGridColors(colors, wordle)
                                    drawLetterGrid()

                                    #Checks if won
                                    if colors == [2, 2, 2, 2, 2]:
                                        displayMessage("You Won")
                                        flag = False
                                    #Checks if lost
                                    elif COLUMN == 5:
                                        displayMessage("You Lose, the word was: " + gameassets.WORDLEWORD)
                                        flag == False

                                    #Update coordinates
                                    COLUMN += 1
                                    ROW = 0
                                    COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE
                                    ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
                                
                                #Displayed if word isn't a wordle word
                                else:
                                    displayMessage("Invalid Word")
                            #Displayed if row isn't filled
                            else:
                                displayMessage("Not Enough Letters")

                        #Any Other Key
                        case _:
                            #Checks if letter
                            if(event.key >= 97 and event.key <= 122):
                                #Checks if row is not filled
                                if(ROW != 5):
                                    s = ALPHABET[event.key - 97]
                                    GRID[COLUMN][ROW] = s
                                    printLetter(s, ROWCOORDS, COLUMNCOORDS, MAINBLOCKSIZE, GRAY)
                                    ROW += 1
                                    COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE
                                    ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
            #If game is quit
            if event.type == pg.QUIT:
                running = False
            pg.display.update()
