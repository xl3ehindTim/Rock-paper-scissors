import random
import os
import math
import time

# Computer options
options = ["rock", "paper", "scissors"]
os.system("CLS")

# User input
print("rock, paper or scissors?")
guess = input()
os.system("CLS")

# Rock, paper, scissors! (countdown)
time.sleep(1)
print("Rock, ")
time.sleep(1)
print("Paper, ")
time.sleep(1)
print("Scissors")
time.sleep(1)
os.system("CLS")
print("Shoot!\n")

# 
while not guess in options:
    print("Please choose rock, paper or scissors")
    guess = input()

computer = math.floor(random.random()*len(options))
computer = options[computer]

# Rock
if guess == "rock":
    if computer is "rock":
        print("Draw!")

    elif computer is "paper":
        print("Rock looses to paper, you loose!")

    else:
        print("Rock beats scissors, you win!")
# Paper
elif guess == "paper":
    if computer is "rock":
        print("Paper beats rock, you win!")
    
    elif computer is "paper":
        print("Draw!")

    else:
        print("Paper loses to scissors, you loose!")
# Scissors
else:
    if computer is "rock":
        print("Scissors looses to rock, you loose!")

    elif computer is "paper":
        print("Scissors beats paper, you win!")

    else:
        print("Draw!")

