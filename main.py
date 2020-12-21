from functions import computer, check_input, user, countdown, winner

# Get user action
user_action = check_input(user())

# Initiate countdown
countdown()

# Get winner/draw
winner(user_action, computer())
