'''
Project # 1 : A Simple Game | CONNECT 4
Connect 4 Game by Hasbro Company (using python)
'''

import sys
from termcolor import colored, cprint

currentField = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]


def drawField(field):
    for row in range(13):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    practicalColumn = int(column / 2)
                    if column != 12:
                        print(field[practicalColumn][practicalRow], end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end = "")
        else:
            print("-" * 13)
    print("_" * 13, "\n") #visual base of boardgame


def Checker():
    stat = 1
    # Check rows for winner
    for row in range(6):
        for col in range(3):
            if (currentField[row][col] == currentField[row][col + 1] == currentField[row][col + 2] ==\
                currentField[row][col + 3]) and (currentField[row][col] != " "):
                stat = 0
                return stat
    # Check columns for winner
    for col in range(6):
        for row in range(3):
            if (currentField[row][col] == currentField[row + 1][col] == currentField[row + 2][col] ==\
                currentField[row + 3][col]) and (currentField[row][col] != " "):
                stat = 0
                return stat
    # Check diagonal (top-left to bottom-right) for winner
    for row in range(3):
        for col in range(4):
            if (currentField[row][col] == currentField[row + 1][col + 1] == currentField[row + 2][col + 2] ==\
                currentField[row + 3][col + 3]) and (currentField[row][col] != " "):
                stat = 0
                return stat
    # Check diagonal (bottom-left to top-right) for winner
    for row in range(5, 2, -1):
        for col in range(3):
            if (currentField[row][col] == currentField[row - 1][col + 1] == currentField[row - 2][col + 2] ==\
                currentField[row - 3][col + 3]) and (currentField[row][col] != " "):
                stat = 0
                return stat
    return stat


def Updater():
    end = False
    player = 1
    while end == False:
        Checker()
        print("Player ", player, "'s turn.")
        MoveRow = int(input("Enter row number: "))
        MoveColumn = int(input("Enter column number: "))
        print('\n')
        if player == 1:
            if currentField[MoveColumn][MoveRow] == " ":
                currentField[MoveColumn][MoveRow] = str(colored(u'\u2B24', 'blue'))
                if Checker() == 1:
                    player = 2
                else:
                    print('Player', player, 'wins!')
                    end = True
            else:
                print('Invalid Move!\n')
                return Updater()
        else:
            if currentField[MoveColumn][MoveRow] == " ":
                currentField[MoveColumn][MoveRow] = str(colored(u'\u2B24', 'red'))
                if Checker() == 1:
                    player = 1
                else:
                    print('Player', player, 'wins!')
                    end = True
            else:
                print('Invalid Move!\n')
                return Updater()
        drawField(currentField)


#Start game
print("Let's play CONNECT 4!\n")
drawField(currentField)
Updater()