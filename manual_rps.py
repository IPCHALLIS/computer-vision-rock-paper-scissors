import random

labels = [Rock, Paper, Scissors]

def get_computer_choice():
    computer_choice = random.choice(labels)
    return computer_choice

def get_user_choice():
    user_choice = input("What\'s your move: Rock, Paper, or Scissors:").lower()
    return user_choice