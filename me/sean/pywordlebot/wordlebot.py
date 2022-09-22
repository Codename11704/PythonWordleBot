
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
        possRes = wc.checkWord(word, possibility)
        isPossible = True
        counter = 0
        while counter <= 4 and isPossible == True:
            print(possRes[counter])
            match results[counter]:

                case 0:
                    if possRes[counter] != 0:
                        pass
                case 1:
                    #if possRes[counter] == 1 or possRes[counter] == 2:
                        #pass
                    #else:
                        #isPossible = False
                    pass
                case 2:
                    pass
                    if possRes[counter] != 2:
                        isPossible = False
            counter += 1

        if isPossible == False:
            #WTF is going on here
            listBuffer.pop(ind)

        ind +=1
    print(listBuffer)
    return listBuffer


def main():
    testWord = "CRANE"
    pg.init()
    ga.init()
    print(ga.WORDLEWORD)
    #CURRENTPOSSIBLESOLUTIONS = ga.WORDS
    CURRENTPOSSIBLESOLUTIONS = ["cxxxx", "xrxxx", "xxaxx", "xxxnx", "xxxxe"]
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    res = wc.checkWord(ga.WORDLEWORD, testWord)
    print(res)
    CURRENTPOSSIBLESOLUTIONS = updateList(testWord, res, CURRENTPOSSIBLESOLUTIONS)
    #print(CURRENTPOSSIBLESOLUTIONS)
    print(CURRENTPOSSIBLESOLUTIONS.__len__())
    

if __name__ == "__main__":
    main()




