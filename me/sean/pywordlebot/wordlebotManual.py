from dataclasses import *
from wordchecker import *
import botassets

def letChoose(list, info):
    i = 0
    for item in list:
        print("[" + str(i) + "] Word: " + item + " Info: " + str(info[i]))
        i+=1
    inp = int(input("Please enter decision: "))
    return list[inp]
        

def main():
    """Promts user input to solve a wordle
    """
    best = "TARES"
    data = botassets.loadInfo()
    print("The best option is: " + best)
    res = botassets.strToTernDec(input("Insert the results of the wordle: "))
    new = data.getIndices(best, res)
    for i in range(0, 4):
        (bestOf, info) = botassets.bestPossibleAnswer(new, data)
        best = letChoose(bestOf, info)
        res = botassets.strToTernDec(input("Insert the results of the wordle: "))
        new = botassets.updateList(best, res, new, data)


if __name__ == "__main__":
    main()




