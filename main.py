try:
    import random
    import math
    import pyttsx3
    #changing voice to girl
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)
    # Computer options
    options = ["rock", "paper", "scissors"]
    # User input
    guess = input("rock, paper or scissors?\n")
    while not guess in options:
        print("Please choose rock, paper or scissors")
        guess = input()

    computer = options[math.floor(random.random()*len(options))]

    # Rock, paper, scissors! (countdown)
    print("Rock, ")
    print("Paper, ")
    print("Scissors")
    pyttsx3.speak("Rock, Paper, Scissor")
    print("Shoot!\n")
    pyttsx3.speak("Shoot")
    # Rock
    if guess == "rock":
        if computer == "rock":
            print("Draw!")
            pyttsx3.speak("Draw")

        elif computer == "paper":
            print("Rock looses to paper, you loose!")
            pyttsx3.speak("Rock looses to paper, you loose!")

        else:
            print("Rock beats scissors, you win!")
            pyttsx3.speak("Rock beats scissors, you win!")
    # Paper
    elif guess == "paper":
        if computer == "rock":
            print("Paper beats rock, you win!")
            pyttsx3.speak("Paper beats rock, you win!")
        
        elif computer == "paper":
            print("Draw!")
            pyttsx3.speak("Draw!")

        else:
            print("Paper loses to scissors, you loose!")
            pyttsx3.speak("Paper loses to scissors, you loose!")

    # Scissors
    else:
        if computer == "rock":
            print("Scissors looses to rock, you loose!")
            pyttsx3.speak("Scissors looses to rock, you loose!")

        elif computer == "paper":
            print("Scissors beats paper, you win!")
            pyttsx3.speak("Scissors beats paper, you win!")

        else:
            print("Draw!")
            pyttsx3.speak("Draw")

except:
    print("Enter the correct spelling")
    pyttsx3.speak("Enter the correct spelling")
