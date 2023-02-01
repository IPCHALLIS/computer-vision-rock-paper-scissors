import random

labels = ['rock', 'paper', 'scissors']

def get_computer_choice():
    computer_choice = random.choice(labels)
    return computer_choice

def get_user_choice():
    user_choice = input("What\'s your move: Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_winner():
    computer = get_computer_choice()
    user = get_user_choice()
    if computer == 'rock' and user == 'scissors':
        print("You lost")
    elif computer == 'paper' and user == 'scissors':
        print("You won!")
    elif computer == 'scissors' and user == 'paper':
        print("You lost")
    elif user == 'rock' and computer == 'scissors':
        print("You won!")
    elif user == 'paper' and computer == 'scissors':
        print("You lost")
    elif user == 'scissors' and computer == 'paper':
        print("You won!")
    else:
        print("It is a tie!")

def play():
    get_winner()

play()