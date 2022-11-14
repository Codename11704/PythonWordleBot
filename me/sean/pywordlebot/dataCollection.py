import pygame as pg
import gameassets as ga
import wordlebotAuto as wb
import botassets
import json
import time
import math
from dataclasses import dataclass


@dataclass
class gameData:
    answer: str
    guesses: list
    moves: int

def saveData(data):
    with open("me\\sean\\pywordlebot\\data.json", 'w') as f:
        json.dump(data, f)
  
        
def calcTime(secs):
    mins = 0
    if secs > 60:
        mins = math.floor(secs/60)
        secs -= mins*60
    string = str(mins) + " minutes and " + str(secs) + " seconds"
    return string


def main():
    info = {}
    pg.init()
    ga.init()
    data = botassets.loadInfo()
    totalGuesses = 0
    totalTime = 0
    i = 0
    list = ga.ANSWERS
    for item in list:
        tic = time.perf_counter()
        (moves, guesses) = wb.soveWordle(item, data)
        toc = time.perf_counter()
        secs = toc-tic
        totalTime+=secs
        totalGuesses+=moves
        info.update({item: gameData(item, guesses, moves)})
        print("Word: " + item)
        print("Moves: " + str(moves))
        print("Time: " + calcTime(secs))
        i+=1
    saveData(info)
    averageMoves = totalGuesses/i
    averageTime = calcTime(totalTime/i)
    print("The average performance was " + str(averageMoves) + " guesses per game.")
    print("The average time was " + averageTime)
    
if __name__ == "__main__":
    main()
    
    
    