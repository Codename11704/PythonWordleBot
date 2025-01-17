
"""
Author: Sean Droll 
Date: 9/10/22

This file contains all the functions used to check how a users guess matches up against the answer
"""
def letterCounts(word):
    """
    Gets the number of times each letter occurs in the word and returns it as a library
    :param word: The word to have it's letters counted
    """
    letterCount = {}

    for letter in word:
        if letter in letterCount.keys():
            val = letterCount.get(letter) + 1
            letterCount.pop(letter)
            letterCount.update({letter: val})
        else:
            letterCount.update({letter: 1})
    return letterCount  


def checkWord(sol, ans):
    """
    This function checks how the user's guess compares against the solution
    and returns an array of colors to be printed on the screen
    :param sol: The wordle solution
    :param ans: The answer given by the user
    :returns: Array of colors that coralate with the letters of the word
    """
    colors = [0, 0, 0, 0 ,0]
    solArr = list(sol)
    gArr = list(ans)
    solLetterCounts = letterCounts(sol)

    for i in range(0, 5):
        letter = gArr[i]
        if solArr[i] == letter:
            colors[i] = 2
            val = solLetterCounts.get(letter) - 1
            solLetterCounts.pop(letter)
            solLetterCounts.update({letter: val})


    for i in range(0, 5):
        letter = gArr[i]
        if colors[i] != 2:
            if list(sol).count(letter) > 0:
                
                if solLetterCounts.get(letter) > 0:
                    colors[i] = 1
                    val = solLetterCounts.get(letter) - 1
                    solLetterCounts.pop(letter)
                    solLetterCounts.update({letter: val})
                else:
                    colors[i] = 0
            else:
                colors[i] = 0

    return colors