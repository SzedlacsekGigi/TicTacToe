import os
import sys
import time
import shutil
import random
from random import randint
import pickle

columns = shutil.get_terminal_size().columns

#Definitions

def drawHeader():
    print((bcolors.HEADER +
           "     _   _      _             _              " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           "    | | (_)    | |           | |             " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           "    | |_ _  ___| |_ __ _  ___| |_ ___   ___  " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           r"    | __| |/ __| __/ _` |/ __| __/ _ \ / _ \ " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           "    | |_| | (__| || (_| | (__| || (_) |  __/ " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           r"     \__|_|\___|\__\__,_|\___|\__\___/ \___| " +
           bcolors.ENDC).center(columns))
    print((bcolors.HEADER +
           "                                             " +
           bcolors.ENDC).center(columns))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menu():
    os.system("clear")
    drawHeader()
    print("                                                                      ")
    print(("Welcome to TicTacToe!").center(columns))
    print("                                                                      ")
    print(("Please choose your game").center(columns))
    print("                                                                      ")
    print(("1: Practice (1 game)").center(columns))
    print("                                                                      ")
    print(("2: Hungarian Truth (3 game)").center(columns))
    print("                                                                      ")
    print(("3: Full Pro (10 game)").center(columns))
    print("                                                                      ")
    print(("4: Against AI").center(columns))
    print("                                                                      ")
    print(("5: High Score").center(columns))
    print("                                                                      ")
    print(("6: Quit").center(columns))
    print("                                                                      ")

    version = input("?")
    os.system("clear")
    if version == "1":
        version = 1
    elif version == "2":
        version = 3
    elif version == "3":
        version = 10
    if version == "4":
        AI == True
    elif version == "5":
        drawHeader()
        print(print_highscore())
    elif version == "6":
        print(("Thank you for playing!").center(columns))
        time.sleep(3)
        sys.exit()
    return version

def ScoreTable():
    print("Player1 Wins : " + str(wins_player1) + "   Player2 Wins : " + str(wins_player2) + "   Tie: " + str(Ties))
    time.sleep(3)

def NewGame():
    os.system("clear")
    newgrid = [["| ", 1, " | ", 2, " | ", 3, " |"],
            ["| ", 4, " | ", 5, " | ", 6, " |"],
            ["| ", 7, " | ", 8, " | ", 9, " |"]]
    movelist = []
    drawHeader()
    drawGrid(newgrid)

def drawGrid(grid):
    for rows in grid:
        print("+---+---+---+")
        for row in rows:
            print(row, end='')
        print()
    print("+---+---+---+")

def winsituation(actualplayerparameter):
    player = actualplayerMove(actualplayerparameter)
    if ((grid[0][1] == player) and (grid[0][3] == player) and (grid[0][5] == player) or
        (grid[1][1] == player) and (grid[1][3] == player) and (grid[1][5] == player) or
        (grid[2][1] == player) and (grid[2][3] == player) and (grid[2][5] == player) or
        (grid[0][1] == player) and (grid[1][1] == player) and (grid[2][1] == player) or
        (grid[0][3] == player) and (grid[1][3] == player) and (grid[2][3] == player) or
        (grid[0][5] == player) and (grid[1][5] == player) and (grid[2][5] == player) or
        (grid[0][1] == player) and (grid[1][3] == player) and (grid[2][5] == player) or
        (grid[0][5] == player) and (grid[1][3] == player) and (grid[2][1] == player)):
        print(player + " Wins")
        return True

def tie():
    if step == 9:
        print("It's a tie!")
        return True

# Global variables
grid = [["| ", 1, " | ", 2, " | ", 3, " |"],
        ["| ", 4, " | ", 5, " | ", 6, " |"],
        ["| ", 7, " | ", 8, " | ", 9, " |"]]
os.system("clear")
movelist = []
step = 0
highscore = {"test":123}


#Game


def players():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Choose your destiny (X or O?)")
        letter = input().upper()
    if letter == "X":
        step = 0
        player1Symbol = bcolors.OKBLUE + "X" + bcolors.ENDC
        player2Symbol = bcolors.OKGREEN + "O" + bcolors.ENDC
        print("Player 1 is X and Player 2 is O")
        time.sleep(1)
    elif letter == "O":
        step = 0
        player1Symbol = bcolors.OKGREEN + "O" + bcolors.ENDC
        player2Symbol = bcolors.OKBLUE + "X" + bcolors.ENDC
        print("Player 1 is O and Player 2 is X")
        time.sleep(1)
    player1Name = "Player1"
    player2Name = "Player2"
    return step, player1Symbol, player2Symbol, player1Name, player2Name


def whogoesfirst():
    value = random.randint(0,1)
    if value == 0:
        return "Player1"
    elif value == 1:
        return "Player2"
    

def actualplayer(actualplayerparameter):
    if actualplayerparameter == "Player1":
        return player1Name
    if actualplayerparameter == "Player2":
        return player2Name


def actualplayerMove(actualplayerparameter):
    if actualplayerparameter == "Player1":
        return player1Symbol
    if actualplayerparameter == "Player2":
        return player2Symbol

def save_highscore(highscore):
    highscore1 = (input(str("Player1, please enter your name: ")))
    if highscore1 not in highscore:
        highscore.update({highscore1:wins_player1})
    else:
        highscore[highscore1]+=wins_player1
    highscore2 = (input("Player2, please enter your name: "))
    if highscore2 not in highscore:
        highscore.update({highscore2:wins_player2})
    else:
        highscore[highscore2]+=wins_player2
    pickle.dump(highscore, open("ttthighscore.p", "wb"))

def print_highscore():
    print(("_   _    _    _     _        ___  _____   _____ _    __  __ _____").center(columns))
    print(("| | | |  / \  | |   | |      / _ \|  ___| |  ___/ \  |  \/  | ____|").center(columns))
    print(("| |_| | / _ \ | |   | |     | | | | |_    | |_ / _ \ | |\/| |  _|  ").center(columns))
    print(("|  _  |/ ___ \| |___| |___  | |_| |  _|   |  _/ ___ \| |  | | |___ ").center(columns))
    print(("|_| |_/_/   \_\_____|_____|  \___/|_|     |_|/_/   \_\_|  |_|_____|\n").center(columns))
    highscore = pickle.load(open("ttthighscore.p", "rb"))
    for key, value in highscore.items():
        print('{} {}'.format (key, value).center(columns))
    print(("Press r to return to the main menu").center(columns))
    if input() == "r":
        os.system("clear")
        version = menu()


step,player1Symbol,player2Symbol, player1Name, player2Name  = players()

step = 0

while True:
    wins_player1 = 0
    wins_player2 = 0
    Ties = 0
    
    for i in range(menu()):
        os.system("clear")
        grid = [["| ", 1, " | ", 2, " | ", 3, " |"],
            ["| ", 4, " | ", 5, " | ", 6, " |"],
            ["| ", 7, " | ", 8, " | ", 9, " |"]]
        movelist = []
        drawHeader()
        drawGrid(grid)
        actualplayerparameter = whogoesfirst()
        while step < 9:
            jatekos = actualplayer(actualplayerparameter)
            try:
                move = int(input(jatekos + ", your move?"))
            except ValueError:
                print("Invalid input")
            else:
                if move in movelist:
                    print("This field is already taken.")
                elif move < 1 or move > 9:
                    print("Invalid input")
                else:
                    movelist.append(move)
                    print(movelist)
                    for i in range(3):
                        for j in range(7):
                            if move == grid[i][j]:
                                grid[i][j] = actualplayerMove(actualplayerparameter)
                                os.system("clear")
                                drawHeader()
                                drawGrid(grid)
                    step += 1
                    if winsituation(actualplayerparameter) == True:
                        if actualplayerparameter == "Player1":
                            wins_player1 = wins_player1 + 1
                        elif actualplayerparameter == "Player2":
                            wins_player2 = wins_player2 + 1
                        ScoreTable()
                        step = 0
                        break
                    if tie() == True:
                        Ties += 1
                        ScoreTable()
                        step = 0
                        break
                    if actualplayerparameter == "Player1":
                        actualplayerparameter = "Player2"
                    elif actualplayerparameter == "Player2":
                        actualplayerparameter = "Player1"
    save_highscore(highscore)
    time.sleep(3)
    os.system("clear")
    valtozat = menu()