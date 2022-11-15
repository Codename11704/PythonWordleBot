import pygame as pg
import gameassets as ga
import wordchecker as wc
from dataclasses import *
import json
import math



TOPWORDS = ["TARES", "LARES", "RALES", "RATES", "NARES", "SOARE", "TALES", "REAIS", "TEARS", "ARLES"]
TOPINFO = [6.19, 6.14, 6.11, 6.09, 6.07, 6.07, 6.06, 6.05, 6.05, 6.03]


@dataclass
class DataMatrix:
    """This dataclass acts as a 2D dictionary to store wordle results by word

    Returns:
        dict: the dictionary storing the data
    """
    dict: dict
    
    def addItem(self, ind1, ind2, val):
        """Adds an item to the matrix

        Args:
            ind1 (any): One index pointing to the value
            ind2 (any): The other index pointing to the value
            val (any): The value being pointed to
        """
        dict = self.dict
        if ind1 in dict.keys():
            self.dict.get(ind1).update({ind2 : val})
        else:
            self.dict.update({ind1 : {ind2 : val}})
            
    def getItem(self, ind1, ind2):
        """Retrieves an item by its indices

        Args:
            ind1 (any): One index pointing to the value
            ind2 (any): The other index pointing to the value

        Returns:
            Any: The value that was stored
        """
        dict1 = self.dict
        dict2 = dict1.get(ind1)
        val = dict2.get(ind2)
        return val
    
    def getIndices(self, ind1, val):
        """Gets a list of indices with val as the value and ind1 as its other index

        Args:
            ind1 (Any): An index that points to val
            val (Any): The value that is stored at ind1 and the returned indices

        Returns:
            List: A list of indices that contain val
        """
        keys = []
        dict = self.dict.get(ind1)
        for key in dict.keys():
            if dict.get(key) == val:
                keys.append(key)
        return keys
        
        
def updateList(word, results, cps, data):
    """Given a word and its results, after being checked, calculates the current possible solutions given the previous current possible solutions

    Args:
        word (str): The word that was guessed
        results (int): An integer that represents the results given by a check
        cps (int): The current possible solutions before the list is updated
        data (DataMatrix): The data matrix containing the results of each wordle check

    Returns:
        list: A list of the new current possible solutions
    """
    #Rather than checking each word if it is a valid solution,
    #We can use a 2d dictionary that contains every combonation of 2
    #Words, and get the valid indices
    possible = data.getIndices(word, results)
    

    #Afterwords we need to compare it to our previous list to get
    #the final list of valid results
    newList = []
    for item in possible:
        if item in cps:
            newList.append(item)
    return newList


def ternaryToDecimal(list):
    """Converts a ternary list into a decimal integer

    Args:
        list (list): A ternary array

    Returns:
        int: The integer representing the ternary list
    """
    n = 0
    ind = 4
    for num in list:
        n += (3**ind)*num
        ind-=1
    return n


def ternary(n):
    """Converts an integer to ternary

    Args:
        n (The integer to convert to ternary): _description_

    Returns:
        list: A ternary list
    """
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
    """Safely performs log2

    Args:
        x (float): The number you wanna take log2 of

    Returns:
        float: log2 of x if x > 0
    """
    return math.log2(x) if x > 0 else 0


def bestPossibleAnswers(list, data):
    """Given a list of words, what is the best possible solutions to solve the wordle

    Args:
        list (list):The current possible solutions
        data (DataMatrix): The data matrix containing the results of each wordle check

    Returns:
       list: The statistical best answer
    """
    #Empty list to store data
    topWords = []
    topInfo = []
    #Go through every word to calculate its average info
    for word1 in list[:]:
        avgInfo = 0
        #For every word we must go thorough every possible result, we can represent these results
        #in ternary, and in turn as a decimal between 0, and 363

        for i in range(0, 363):

            #We can see how much the list is reduced by,
            #to see how much this word has helped us in respect to its result
            oldList = list[:]
            newList = updateList(word1, i, oldList, data)
            prob = len(newList)/len(oldList)

            #So long as we still receive information from this result, we add it to
            #avg info
            if prob != 0:
                info = (safe_log2(1/prob))
                avgInfo += prob*info

        #We will rank all the words by their avg info, and return the top 10
        i = (len(topInfo)-1)
        while i != -1 and avgInfo > topInfo[i]:
            i-=1
        topInfo.insert(i+1, avgInfo)
        topWords.insert(i+1, word1)
    return (topWords[:11], topInfo[:11])
            
                
        


def create_matrix(lst):
    """Creates a data matrix of all wordle checks and tracks its progress

    Args:
        l1 (list): A list containing every possible wordle intput

    Returns:
        DataMatrix: A matrix of every possivle wordle result
    """
    dm = DataMatrix({})
    prog = 0
    perc = 0
    for word1 in lst:
        for word2 in lst:
            res = wc.checkWord(word1, word2)
            resInt = ternaryToDecimal(res)
            dm.addItem(word2, word1, resInt)
        prog+=1
        if perc < math.floor((prog/len(lst))*100):
            perc = math.floor((prog/len(lst))*100)
            print("Progress: " + str(perc) + "%")
    return dm


def saveInfo():
    """Creates a datamatrix and saves it to a file, only need to run once
    """
    pg.init()
    ga.init()
    list1 = ga.WORDS
    
    table = create_matrix(list1)
    with open("me\\sean\\pywordlebot\\assets\\DataMatrix.json", 'w') as f:
        json.dump(table.dict, f)
    
    
def loadInfo():
    """Loads a data matrix from a file

    Returns:
        DataMatrix: A data matrix of the contents of the file
    """
    with open("me\\sean\\pywordlebot\\assets\\DataMatrix.json", 'r') as f:
        d = json.load(f)
        newTable = DataMatrix(d)
        return newTable
    
    
def strToTernDec(str):
    """Concerts a string of numbers into a list of ints

    Args:
        str (str):The string you want to convert to a list

    Returns:
        int: The inputted string converted to an integer representation of a ternary list
    """
    arr = []
    for char in str:
        arr.append(int(char))
    return ternaryToDecimal(arr)


def bestStarter():
    """Calculates to best starting guess for wordle, only need to run once
    """
    pg.init()
    ga.init()
    data = loadInfo()
    list = ga.WORDS
    (bestOf, info) = bestPossibleAnswers(list, data)
    
    print(bestOf)
    print(info)
    

if __name__ == "__main__":
    bestStarter()
    
    