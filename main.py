import random
import os
import math
import time

# Computer options
options = ["rock", "paper", "scissors"]
os.system("cls | clear")

# User input
guess = input("rock, paper or scissors?\n")
os.system("cls | clear")

while not guess in options:
    print("Please choose rock, paper or scissors")
    guess = input()

computer = options[math.floor(random.random()*len(options))]

# Rock, paper, scissors! (countdown)
time.sleep(1)
print("Rock, ")
time.sleep(1)
print("Paper, ")
time.sleep(1)
print("Scissors")
time.sleep(1)
os.system("cls | clear")
print("Shoot!\n")

# Rock
if guess == "rock":
    if computer == "rock":
        print("Draw!")

    elif computer == "paper":
        print("Rock looses to paper, you loose!")

    else:
        print("Rock beats scissors, you win!")

# Paper
elif guess == "paper":
    if computer == "rock":
        print("Paper beats rock, you win!")
    
    elif computer == "paper":
        print("Draw!")

    else:
        print("Paper loses to scissors, you loose!")

# Scissors
else:
    if computer == "rock":
        print("Scissors looses to rock, you loose!")

    elif computer == "paper":
        print("Scissors beats paper, you win!")

    else:
        print("Draw!")
