
from operator import truediv
import pygame as pg
import math
import gameassets

SIZE = WIDTH, HEIGHT = 600, 700
MAINBLOCKSIZE = math.floor(math.sqrt(HEIGHT*WIDTH*.013))
GRID = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
ALPHABETQWERTY = list("qwertyuiopasdfghjklzxcvbnm")

ROW = 0
COLUMN = 0

ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (201, 201, 201)

def drawMainGrid():
    gridWidth = 5*MAINBLOCKSIZE
    gridHeight = 6*MAINBLOCKSIZE
    xmargin = (WIDTH - gridWidth)//2
    ymargin = math.floor(MAINBLOCKSIZE*(2/3))
    for x in range(xmargin, xmargin + gridWidth, MAINBLOCKSIZE):
        for y in range(ymargin, ymargin + gridHeight, MAINBLOCKSIZE):
            rect = pg.Rect(x, y, MAINBLOCKSIZE, MAINBLOCKSIZE)
            pg.draw.rect(SCREEN, BLACK, rect, 1)


def drawLetterGrid():
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
        printLetter(ALPHABETQWERTY[counter], x, y, blockSize)
        counter +=1
        rect = pg.Rect(x, y, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect, 1) 


    for x in range(xmargin2, xmargin2 + gridWidth2, blockSize):
        printLetter(ALPHABETQWERTY[counter], x, y + blockSize, blockSize)
        counter +=1
        rect = pg.Rect(x, y + blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect, 1) 

    for x in range(xmargin3, xmargin3 + gridWidth3, blockSize):
        printLetter(ALPHABETQWERTY[counter], x, y + 2*blockSize, blockSize)
        counter +=1
        rect = pg.Rect(x, y + 2*blockSize, blockSize, blockSize)
        pg.draw.rect(SCREEN, BLACK, rect, 1) 



def printLetter(s, x, y, rectSize):
    if s == "":
        rect1 = pg.Rect(x, y, rectSize, rectSize)
        pg.draw.rect(SCREEN, GRAY, rect1)
        rect2 = pg.Rect(x, y, rectSize, rectSize)
        pg.draw.rect(SCREEN, BLACK, rect2, 1)
    else:
        text = gameassets.FONT.render(s.upper(), True, BLACK, GRAY)
        textRect = text.get_rect()
        textRect.center = (x + rectSize//2, y + rectSize//2)
        SCREEN.blit(text, textRect)
    

def listToString(s):
    str1 = ""

    for char in s:
        str1 += char

    return str1

def checkIfValid(s):
    print(s.upper())
    if gameassets.WORDS.__contains__(str(s).upper()):
        return True
    else:
        return False


#gameloop
if __name__ == "__main__":
    global SCREEN
    pg.init()
    gameassets.init()
    
    pg.display.set_caption("Wordle Bot")
    pg.display.set_icon(gameassets.ICON)
    SCREEN = pg.display.set_mode(SIZE)
    SCREEN.fill(GRAY)
    drawMainGrid()
    drawLetterGrid()

    running = True
    while running:

        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                print(event.key)
                
                match event.key:
                    case 8:
                        if ROW == 0:
                            pass
                        else:
                            ROW = ROW - 1
                            GRID[COLUMN][ROW] = ""
                            ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
                            printLetter("", ROWCOORDS, COLUMNCOORDS, MAINBLOCKSIZE)
                        break
                    case 13:
                        if(ROW == 5):
                            if(checkIfValid(listToString(GRID[COLUMN]))):
                                print("Valid")
                                COLUMN += 1
                                ROW = 0
                                COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE
                                ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
                                
                                
                            else:
                                print("Invalid")
                        else:
                            print("Incomplete")

                        break
                    case _:
                        if(event.key >= 97 and event.key <= 122):
                    
                            if(ROW != 5):
                                s = ALPHABET[event.key - 97]
                                GRID[COLUMN][ROW] = s
                                printLetter(s, ROWCOORDS, COLUMNCOORDS, MAINBLOCKSIZE)
                                ROW += 1
                                COLUMNCOORDS = (2*MAINBLOCKSIZE)//3 + COLUMN*MAINBLOCKSIZE
                                ROWCOORDS = ((WIDTH - 5*MAINBLOCKSIZE)//2) + ROW*MAINBLOCKSIZE
                        break
                
            if event.type == pg.QUIT:
                running = False
            pg.display.update()
