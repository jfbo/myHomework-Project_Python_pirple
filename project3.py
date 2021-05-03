"""
Project # 3 : Pick A Card Game!
"""

'''
"War" Card Game
https://hobbylark.com/card-games/How-to-Play-the-War-Card-Game

Note: My 'War' Card Game rules and flow is slightly modified to be more engaging in python. Thanks!
    - Players now know their own card set and can choose their card for every round.
'''
from random import shuffle
from termcolor import colored

deck = []
DeckP1 = []
DeckP2 = []
colored(DeckP1, 'blue')
colored(DeckP2, 'red')

for i in range(4):
    for card in range(2,15):
        deck.append(str(card))
shuffle(deck)
for i in range(52):
    cardP = deck.pop()
    if i % 2 == 0:
        DeckP1.append(cardP)
    elif i % 2 != 0:
        DeckP2.append(cardP)

def compareCard(DeckP1, DeckP2):
        p1c = DeckP1.pop(player1card)
        p2c = DeckP2.pop(player2card)
        print(p1n + "'s card -", colored(p1c, 'blue'), " | ", p2n + "'s card -", colored(p2c, 'red'))

        if p1c > p2c:
            print(p1n, "wins round", round, "\n")
            DeckP1.append(p1c)
            DeckP1.append(p2c)
        elif p2c > p1c:
            print(p2n, "wins round", round, "\n")
            DeckP2.append(p2c)
            DeckP2.append(p1c)
        elif p1c == p2c:
            print(colored("\n WAR!!! \n", 'yellow'))
            anykey = input("\nPress any key to continue ")
            compareCard(DeckP1, DeckP2)


print("The 'War' Card Game\n")
print("*-*-*  GAME INSTRUCTIONS  *-*-*\n")
print("> Each player will have 26 cards during the start of the game. It will be shown as a dictionary | IndexNumber:CardValue")
print("> For every round, each player will pick a card from their own set. (Input the Index Number from the dictionary.)")
print("> Card picked by each player will be revealed, and whoever has the highest value wins the round and will acquire both cards placed.")
print("> If both cards are of the same value, 'War' occurs...")
print("> Players will pick another card from their set to battle, and whoever has the highest value wins the round and gets both cards.")
print("> The game continues until one person runs out of cards.\n")
print("Lowest to Highest:  2, 3, 4, 5, 6, 7, 8, 9, 10, 11-J, 12-Q, 13-K, 14-A\n")

p1n = str(input("Player 1 | Type your name:  "))
p2n = str(input("Player 2 | Type your name:  "))
print(chr(27) + "[2J")
print("Starting the game . . .")
anykey = input("\nPress any key to start | ")

round = 0
while DeckP1 and DeckP2:
    ddp1 = {i : DeckP1[i] for i in range(0, len(DeckP1))}
    ddp2 = {i : DeckP2[i] for i in range(0, len(DeckP2))}
    round += 1

    print(chr(27) + "[2J")
    print("Round", round, "|", p1n + "'s turn . . .\n")
    print(ddp1, "\n")
    player1card = int(input("Pick your card (type the key number - left integer in the dictionary): "))
    print(chr(27) + "[2J")
    print("Round", round, "|", p2n + "'s turn . . .\n")
    print(ddp2, "\n")
    player2card = int(input("Pick your card (type the key number - left value in the dictionary): "))
    print(chr(27) + "[2J")

    print("ROUND", round)
    print("\nFlipping both cards...")
    anykey = input("\nPress any key to continue")
    print(chr(27) + "[2J")

    compareCard(DeckP1, DeckP2)
    print("Summary . . .")
    print(p1n + "'s # of cards:", len(DeckP1), "|", p2n + "'s # of cards:", len(DeckP2))
    anykey = input("\nPress any key for next round")

