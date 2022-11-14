import pygame as pg
import gameassets as ga
import wordchecker as wc
from dataclasses import *
import json
import math

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

def ternary(n):
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
                avgInfo += prob*info
        print("Word: " + word1 + " Info: " + str(avgInfo))
        if avgInfo >= mostData:
            bestWord = word1
            mostData = avgInfo
    return bestWord

def create_table(l1, l2):
    md = multiDict({})
    prog = 0
    perc = 0
    for word1 in l1:
        for word2 in l2:
            res = wc.checkWord(word1, word2)
            resInt = ternaryToDecimal(res)
            md.addItem(word2, word1, resInt)
        prog+=1
        if perc < math.floor((prog/len(l1))*100):
            perc = math.floor((prog/len(l1))*100)
            print("Progress: " + str(perc) + "%")
    return md

def saveInfo():
    pg.init()
    ga.init()
    list1 = ga.WORDS
    
    table = create_table(list1, list1)
    with open("me\\sean\\pywordlebot\\assets\\map.json", 'w') as f:
        json.dump(table.dict, f)
    
def loadInfo(): 
    with open("me\\sean\\pywordlebot\\assets\\map.json", 'r') as f:
        d = json.load(f)
        newTable = multiDict.from_dict(d)
        return newTable

def bestStarter():
    pg.init()
    ga.init()
    data = loadInfo()
    list = ga.WORDS
    best = bestPossibleAnswer(list, data)
    print("The best possible answer is: " + best)



if __name__ == "__main__":
    bestStarter()
    
    