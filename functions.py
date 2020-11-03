import random
import os
import math
import time

# Define options
options = ["rock", "paper", "scissors"]

# Define constants
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"


def computer():
    """
    Get computer action
    """
    action = options[math.floor(random.random()*len(options))]
    return action


def check_input(action):
    """
    Check user input
    """
    while action not in options:
        action = user()
    return action


def user():
    """
    Get user input
    """
    print("Choose rock, paper or scissors")
    action = input()
    return action


def countdown():
    """ 
    Countdown
    """
    for option in options:
        print(f"{option},")
        time.sleep(1)
        clear_screen()
    print("Shoot!\n")


def rock(action):
    """ User: Rock """
    if action == PAPER:
        return "Rock loses to paper, you lose!"
    return "Rock beats scissors, you win!"


def paper(action):
    """ User: paper """
    if action == ROCK:
        return"Paper beats rock, you win!"
    return "Paper loses to scissors, you lose!"


def scissors(action):
    """ User: scissors """
    if action == ROCK:
        return "Scissors loses to rock, you lose!"
    return "Scissors beats paper, you win!"


def winner(user_action, computer_action):
    """
    Get winner/loser or draw
    """
    List = {
        ROCK: rock,
        PAPER: paper,
        SCISSORS: scissors,
    }

    if user_action != computer:
        print(List[user_action](computer_action))
    else:
        print("Draw!")


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
