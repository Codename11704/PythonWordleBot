
import wordchecker as wc
import gameassets as ga
import pygame as pg
import numpy
from wordchecker import *

CURRENTPOSSIBLESOLUTIONS = []

def updateList(word, results, cps):
    newList = cps.copy()
    
    for possibility in cps:
        counts = letterCounts(possibility)
        feesible = True
        for i in range(5):
            lett = word[i]
            if results[i] == 2:
                if possibility[i] == lett:
                    val = counts.get(lett)-1
                    counts.update({lett : val})
                else:
                    newList.remove(possibility)
                    i = 5
                    feesible = False
                    break
            elif results[i] == 0:
                if possibility[i] == lett:
                    newList.remove(possibility)
                    i = 5
                    feesible = False
                    break
        if feesible:
            for i in range(5):
                lett = word[i]
                if results[i] == 1:
                    if lett in possibility:
                        if counts.get(lett) == 0:
                            newList.remove(possibility)
                            i == 4
                            break
                        else:
                            val = counts.get(lett)-1
                            counts.update({lett : val})
                    else:
                        newList.remove(possibility)
                        i == 4
                        break
    if len(newList) == 0:
        return cps
    else:
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




