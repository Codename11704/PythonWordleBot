
"""
in this file, sol is the solution to the wordle while answer is the answer the user has given
"""



from turtle import color


def countLetters(word, lett):
    num = 0
    for letter in word:
        if letter == lett:
            num +=1
    return num

def isCurrentLetterPossible(sol, ans, index):
    solArr = list(sol)
    lett = solArr[index]
    
    if countLetters(ans, lett) >= lettersBefore(sol, index):
        return True
    return False

def letterCounts(word):
    letterCount = {}

    for letter in word:
        if not letter in letterCount.keys():
            letterCount.pop(letter, 1)
        else:
            letterCount.update(letter, (letterCount.get(letter) + 1))
    return letterCount



def checkWord(sol, ans):
    colors = []
    solArr = list(sol)
    gArr = list(ans)
    

    for i in range(0, 5):
        print("Answer: " + solArr[i] + " Guess: " + gArr[i])
        if solArr[i] == gArr[i]:
            colors.append(2)

        
    return colors

            



def lettersBefore(sol, index):
    wordAsArr = list(sol)
    letter = wordAsArr[index]
    num = 0
    
    for i in range (0, index):
        if wordAsArr[i] == letter:
            num += 1

    return num


if __name__ == "__main__":
    #print(countLetters("solds", 'o'))

    #print(lettersBefore("opools", 0))
    #print(countLetters("aaaaa", "b"))
    #print(isCurrentLetterPossible("aaaaa", "bbbbb", 3))

    #print(checkWord("crane", "snane"))

    print(letterCounts("snane"))