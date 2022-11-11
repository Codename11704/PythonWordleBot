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

def safe_log2(x):
    return math.log2(x) if x > 0 else 0

    


def bestPossibleAnswer(list):
    bestWord = ""
    mostData = 0
    for word1 in list[:]:
        avgInfo = 0
        for i in range(0, 363):
            oldList = list[:]
            res = ternary(i)
            newList = wb.updateList(word1, res, oldList)
            prob = len(newList)/len(oldList)
            avgInfo+= prob*(safe_log2(1/prob))
        print("Word: " + word1 + " Info: " + str(avgInfo))
        if avgInfo > mostData:
            bestWord = word1
    print("Best Word: " + bestWord)







        


def main():
    pg.init()
    ga.init()
    init()
    POSSSOL = ga.WORDS
    bestPossibleAnswer(POSSSOL)




if __name__ == "__main__":
    main()