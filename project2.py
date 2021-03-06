"""
Project # 2 : Hangman
"""
#Play hangman in 2-player mode. The game should start by prompting player 1 to pick a word. 
#Then the screen should clear itself so that player 2 can't see the word. |  hint: print(chr(27) + "[2J") 
#After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should be allowed to guess letters until they either win, or lose. 
#As they choose correct letters, the letters should appear on the screen in place of the blank space (clear and redraw the whole screen). 
#As they choose wrong letters, the "man" himself should come end up being drawn, piece by piece. How many guesses they get before losing is up to you 
#Try finding a large list of dictionary words and embedding them in your application. 
#When the game starts, instead of player 1 choosing the word to play with, the computer should pick a random word from the dictionary. 
#This will allow you to play against the computer instead of only 2-player mode. When the game starts, the user should be prompted to choose between 1-player or 2-player mode.



#import random
from nltk.corpus import words
import sys
from termcolor import colored

print("\n*-*-*-*-*-*-*-*-*-*-*-*")
print("* Let's Play Hangman! *")
print("*-*-*-*-*-*-*-*-*-*-*-*\n")

#Drawing Set 0 - 7 index
StickDrawing = [
    " ",

    ("   _______\n" + 
    "         |\n" + 
    "         |\n" + 
    "         |\n" + 
    "         |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    "         |\n" + 
    "         |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    "  |      |\n" + 
    "         |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    " /|      |\n" + 
    "         |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    " /|\     |\n" + 
    "         |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    " /|\     |\n" + 
    " /       |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "         |\n" + 
    "  O      |\n" + 
    " /|\     |\n" + 
    " / \     |\n" + 
    "         |\n"),

    ("   _______\n" + 
    "  |      |\n" + 
    "  O      |\n" + 
    " /|\     |\n" + 
    " / \     |\n" + 
    "         |\n")
]


def letterCheck(secretword):
    wrongLetters = []
    answerLetters = []
    rightLetters = list(secretword)
    
    blanks = int(len(secretword))
    print("It is a", blanks, "- letter word: ")
    for i in range(blanks):
        answerLetters.append(" _")
    print("".join(answerLetters))

    StickDrawingCounter = 0
    while StickDrawingCounter < 7:
        letters = str(input('Guess a letter:  '))
        print(chr(27) + "[2J")

        if letters in secretword:
            print(StickDrawing[StickDrawingCounter])
            print(colored('\nCORRECT GUESS!', 'blue'))
            print("Wrong letters guessed so far... ", wrongLetters, " \n")

            counter = 0
            for sw in rightLetters:
                if letters == sw:
                    answerLetters[counter] = letters
                counter += 1

            ansL = " ".join(answerLetters)
            print(colored(ansL, 'green'))

        else:
            StickDrawingCounter += 1
            print(StickDrawing[StickDrawingCounter])
            print(colored('\nWRONG GUESS!', 'red'))
            wrongLetters.append(letters)
            print("Wrong letters guessed so far... ", wrongLetters, " \n")
            ansL = " ".join(answerLetters)
            print(colored(ansL, 'green'))

        #StrLs = "".join(rightLetters)
        if answerLetters == rightLetters:
            print(colored('\nY O U    W I N   ! ! !\n', 'yellow'))
            break

        if StickDrawingCounter == 7:
            print(colored('\nG A M E   O V E R   ! ! !\n', 'yellow'))
            break

def gamestart():
    print("1-player mode or 2-player mode?")
    players = int(input('Enter: "1" or "2" ----  '))

    if players == 1:
        print("\nYou have chosen 1-player mode.\n")
        #wordbank = ['spring', 'summer', 'autumn', 'winter', 'python', 'java']
        #secretword = random.choice(wordbank)
        secretword = words.words()
        letterCheck(secretword)
        return secretword

    elif players == 2:
        print("\nYou have chosen 2-player mode.\n")
        secretword = str(input("PLAYER 1 - Type the word:  "))
        print(chr(27) + "[2J") 
        print("PLAYER 2")
        letterCheck(secretword)
        return secretword

    else:
        gamestart()

gamestart()
