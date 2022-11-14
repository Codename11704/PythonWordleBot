
import wordchecker as wc
import gameassets as ga
import pygame as pg
from dataclasses import *
from wordchecker import *
import math
import json

@dataclass
class multiDict:
    dict: dict
    
    def addItem(self, ind1, ind2, val):
        dict = self.dict
        if ind1 in dict.keys():
            self.dict.get(ind1).update({ind2 : val})
        else:
            self.dict.update({ind1 : {ind2 : val}})
            
    def getItem(self, ind1, ind2):
        dict1 = self.dict
        dict2 = dict1.get(ind1)
        val = dict2.get(ind2)
        return val
    
    def getIndices(self, ind1, val):
        keys = []
        dict = self.dict.get(ind1)
        for key in dict.keys():
            if dict.get(key) == val:
                keys.append(key)
        return keys
                
    def toDict(self):
        return { "data" : self.dict}
    
    def from_dict(d):
        return multiDict(d)


def updateList(word, results, cps, data):
    possible = data.getIndices(word, results)
    newList = []
    for item in possible:
        if item in cps:
            newList.append(item)
    return newList


def ternaryToDecimal(list):
    n = 0
    ind = 4
    for num in list:
        n += (3**ind)*num
        ind-=1
    return n

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

def bestPossibleAnswer(list, data):
    bestWord = ""
    mostData = 0
    for word1 in list[:]:
        avgInfo = 0
        for i in range(0, 363):
            oldList = list[:]
            res = ternary(i)
            newList = updateList(word1, res, oldList, data)
            prob = len(newList)/len(oldList)
            if prob != 0:
                info = (safe_log2(1/prob))
                avgInfo+= prob*info
        if avgInfo >= mostData:
            bestWord = word1
            mostData = avgInfo
    return bestWord

def loadInfo(): 
    with open("me\\sean\\pywordlebot\\assets\\map.json", 'r') as f:
        d = json.load(f)
        newTable = multiDict.from_dict(d)
        return newTable


def soveWordle(wordle, data):
    best = "TARES"
    pg.init()
    ga.init()
    print("The word is: " + wordle)
    
    res = []
    new = []
    win = False
    if best == wordle:
        win = True
    else:
        res = wc.checkWord(wordle, best)
        print(best)
        print(res)
        new = data.getIndices(best, ternaryToDecimal(res))
    
    i = 1
    while not win and i <= 5:
        best = bestPossibleAnswer(new, data)
        print(best)
        if best == wordle:
            win = True
        else:
            res = wc.checkWord(wordle, best)
            print(res)
            new = updateList(best, ternaryToDecimal(res), new, data)
        i+=1
    
    return 0
    





