
import wordchecker as wc
import gameassets as ga
import pygame as pg



def updateList(word, results, cps):
    listBuffer = cps
    ind = 0
    
    for poss in cps:
        
        i = 0
        isPoss = True
        while i <= 4 and isPoss:
            
            match results[i]:
                case 0:
                    if word[i] == poss[i]:
                        isPoss = False
                case 1:
                    pass
                case 2:
                    if word[i] != poss[i]:
                        print(word[i])
                        print(poss[i])
                        isPoss = False
            i += 1
        if not isPoss:
               listBuffer.pop(ind)
        ind += 1        
    return listBuffer
    


def main():
    currentPossibleSolutions = []
    testWord = "CRANE"
    
    
    pg.init()
    ga.init()
    print(ga.WORDLEWORD)
    
    #CURRENTPOSSIBLESOLUTIONS = ga.WORDS
    currentPossibleSolutions = ["CXXXX", "XRXXX", "XXAXX", "XXXNX", "XXXXE"]
    print(currentPossibleSolutions.__len__())
    res = wc.checkWord(ga.WORDLEWORD, testWord)
    print(res)
    currentPossibleSolutions = updateList(testWord, res, currentPossibleSolutions)
    print(currentPossibleSolutions)
    print(currentPossibleSolutions.__len__())
    
    

if __name__ == "__main__":
    main()




