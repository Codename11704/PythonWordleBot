
import wordchecker as wc
import gameassets as ga
import pygame as pg

CURRENTPOSSIBLESOLUTIONS = []

def updateList(word, results, cps):
    listBuffer = cps
    print(listBuffer.__len__())
    print("Running")
    ind = 0
    for possibility in listBuffer:
        i = 0
        isPossible = True
        while i < 5 and isPossible == True:
            match results[i]:
                case 0:
                    if word[i] == possibility[i]:
                        isPossible = False
                case 1:
                    pass
                case 2:
                    if word[i] != possibility[i]:
                        isPossible = False
            i += 1
        if isPossible == False:
            listBuffer.pop(listBuffer.indexOf(possibility))
    print(listBuffer)
    return listBuffer


def main():
    testWord = "CRANE"
    pg.init()
    ga.init()
    print(ga.WORDLEWORD)
    #CURRENTPOSSIBLESOLUTIONS = ga.WORDS
    CURRENTPOSSIBLESOLUTIONS = ["CXXXX", "XRXXX", "XXAXX", "XXXNX", "XXXXE"]
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    res = wc.checkWord(ga.WORDLEWORD, testWord)
    print(res)
    CURRENTPOSSIBLESOLUTIONS = updateList(testWord, res, CURRENTPOSSIBLESOLUTIONS)
    #print(CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    

if __name__ == "__main__":
    main()




