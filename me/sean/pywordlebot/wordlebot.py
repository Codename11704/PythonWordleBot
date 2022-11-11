
import wordchecker as wc
import gameassets as ga
import pygame as pg
import numpy
from wordchecker import *

CURRENTPOSSIBLESOLUTIONS = []

def updateList(word, results, cps):
    newList = cps.copy()

    for poss in cps:
        res = wc.checkWord(word, poss)
        if res != results:
            newList.remove(poss)
    if len(newList) == 0:
        return cps
    return newList
                            

                    


                
                



def main():
    testWord = "CRANE"
    pg.init()
    ga.init()
    print(ga.WORDLEWORD)
    CURRENTPOSSIBLESOLUTIONS = ga.WORDS
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    res = wc.checkWord(ga.WORDLEWORD, testWord)
    print(res)
    CURRENTPOSSIBLESOLUTIONS = updateList(testWord, res, CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    

if __name__ == "__main__":
    main()




