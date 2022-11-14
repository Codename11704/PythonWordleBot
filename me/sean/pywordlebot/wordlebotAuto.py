
import wordchecker as wc
from dataclasses import *
from wordchecker import *
import botassets

def soveWordle(wordle, data):
    """Automatically solves a wordle and returns the game data

    Args:
        wordle (str): The wordle to solve
        data (DataMatrix): The data matrix containing the results of each wordle check

    Returns:
        (Tuple (int, list)): A tuple containing the amount of tries it took to guess the Wordle and the guesses it made
    """
    best = "TARES"
    guesses = [best]
    res = []
    new = []
    win = False
    if best == wordle:
        win = True
    else:
        res = wc.checkWord(wordle, best)
        new = data.getIndices(best, botassets.ternaryToDecimal(res))
    i = 1
    while not win and i <= 5:
        (bestOf, info) = botassets.bestPossibleAnswer(new, data)
        best = bestOf[0]
        guesses.append(best)
        if best == wordle:
            win = True
        else:
            res = wc.checkWord(wordle, best)
            new = botassets.updateList(best, botassets.ternaryToDecimal(res), new, data)
            i+=1
    
    return (i, guesses)
    





