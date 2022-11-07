
import wordchecker as wc
import gameassets as ga
import pygame as pg
import numpy

CURRENTPOSSIBLESOLUTIONS = []

def updateList(word, results, cps):
    wordLetterCounts = wc.letterCounts(word)
    copy = cps[:]

    
    for possibility in cps[:]:
        possLetterCounts = wc.letterCounts(possibility)


        ind = 0
        isPossible = True
        while ind < 5 and isPossible == True:

            match results[ind]:
                case 0:
                    if word[ind] == possibility[ind]:
                        isPossible = False
                    
                case 1:
                    ch = word[ind]
                    if ch == possibility[ind]:
                        isPossible = False
                    else:
                        if possibility.count(ch) > 0:
                            if possLetterCounts.get(ch) > 0:
                                possLetterCounts.update({ch: (possLetterCounts.get(ch)-1)})
                            else:
                                isPossible = False
                        else:
                            isPossible = False

                case 2:
                    if word[ind] != possibility[ind]:
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
    CURRENTPOSSIBLESOLUTIONS = ga.WORDS
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    res = wc.checkWord(ga.WORDLEWORD, testWord)
    print(res)
    CURRENTPOSSIBLESOLUTIONS = updateList(testWord, res, CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    

if __name__ == "__main__":
    main()




