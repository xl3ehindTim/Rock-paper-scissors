from functions import computer, check_input, user, countdown, winner

# Get computer and user action
computer_action = computer()
user_action = check_input(user())

# Initiate countdown
countdown()

# Get winner/draw
winner(user_action, computer_action)