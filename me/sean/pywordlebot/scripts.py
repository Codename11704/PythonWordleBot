import pygame as pg
import gameassets as ga
import wordchecker as wc
import numpy as np
import bottest as bt

def ternaryToDecimal(list):
    n = 0
    ind = 4
    for num in list:
        n += (3**ind)*num
        ind-=1
    return n


def create_table(l1, l2):
    comboArray = np.empty((12972, 12972))
    ind = 0
    for word1 in l1:
        ind2 = 0
        for word2 in l2:
            res = wc.checkWord(word1, word2)
            dec = ternaryToDecimal(res)
            comboArray[ind, ind2] = dec
            ind2 +=1
        


        ind+=1
        if (ind%130) == 0:
            print(str((ind/12972)*100) + "%")
    return comboArray




def main():
    pg.init()
    ga.init()
    list1 = ga.WORDS
    list2 = ga.WORDS
    
    combos = create_table(list1, list2)

    file = open("wordlecombos.txt", 'w')
    np.savetxt(file, combos)
    file.close()

def main2():
    pg.init()
    ga.init()
    list1 = ga.WORDS
    res = wc.checkWord(list1[234], list1[567])
    print(list1[234])
    print(list1[567])
    print(res)



    num = ternaryToDecimal(res) 
    file = open("wordlecombos.txt", 'r') 
    arr = np.loadtxt(file).astype(np.int64)


    
    arr2 = np.asarray(np.where(arr == num)).T.tolist()
    arr3 = np.asarray(np.where(arr2 == 234)).T.tolist()

    newList = []
    for list in arr3:
        print(list1[list[1]])
        print(wc.checkWord(list1[234], list1[list[1]]))
    




    



if __name__ == "__main__":
    main2()
    