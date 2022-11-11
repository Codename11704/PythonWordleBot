import json
import pygame as pg
import gameassets as ga
import wordchecker as wc
import numpy as np
import bottest as bt
from dataclasses import *

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
        for key in dict.keys:
            if dict.get(key) == val:
                keys.append(key)
                
    def toDict(self):
        return { "data" : self.dict}
    
    def from_dict(d):
        return multiDict(d.get("data"))
        
        
        





def ternaryToDecimal(list):
    n = 0
    ind = 4
    for num in list:
        n += (3**ind)*num
        ind-=1
    return n


def create_table(l1, l2):
    md = multiDict({})
    prog = 0
    for word1 in l1:
        for word2 in l2:
            res = wc.checkWord(word1, word2)
            md.addItem(word1, word2, res)
        prog+=1
        perc = (prog/len(l1))*100
        print("Progress: " + str(perc) + "%")
    return md
    


def main():
    print(ternaryToDecimal([3, 3, 3, 3, 3]))

def main2():
    pg.init()
    ga.init()
    list1 = ga.WORDS
    
    table = create_table(list1, list1)
    with open("me\\sean\\pywordlebot\\assets\\map.json", 'w') as f:
        json.dump(table.toDict(), f)


    with open("me\\sean\\pywordlebot\\assets\\map.json", 'r') as f:
        d = json.load(f)
        newTable = multiDict.from_dict(d)
        print(newTable.getItem("helps", "cants"))
    
    



if __name__ == "__main__":
    main2()
    