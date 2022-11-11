import wordlebot as wb
import gameassets as ga
import wordchecker as wc
import pygame as pg
import math

POSSSOL = []
dataFromWords = {}

def init():
    POSSSOL = ga.WORDS

def ternary (n):
    if n == 0:
        return [0, 0, 0, 0, 0]
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(r)
    res = [0, 0, 0, 0, 0]
    ind = 4
    for n in nums:
        res[ind] = n
        ind-=1
    return res


    


def bestPossibleAnswer(list):
    wordData = {}
    size = len(list)
    ind = 0
    for word1 in list[:]:
        avginfo = 0
        ind2 = 0
        while ind2 < 3**5:
            fakeRes = ternary(ind2)
            newList = list[:]
            newList = wb.updateList("WEARY", fakeRes, newList)

            
            listLen = len(newList)
            prob = listLen/size
            info = math.log2(1/prob)

            print("Combination: " + str(fakeRes) + " List After :" + str(listLen) +  " Probability: " + str(listLen/size) + " Information: " + str(info))
            avginfo = avginfo + (info * prob)
            ind2+=1
        wordData.update({"Weary": avginfo})


        ind += 1
        if(ind%130 == 0):
            print(str(ind%130+1) + "%")
        print(wordData)
        
        
        
    return wordData







        


def main():
    pg.init()
    ga.init()
    init()
    POSSSOL = ga.WORDS
    print(len(POSSSOL))
    dataFromWords = bestPossibleAnswer(POSSSOL)
    print(dataFromWords)




if __name__ == "__main__":
    main()