import random


def get_computer_choice():
    labels = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(labels)
    return computer_choice


def get_user_choice():
    user_choice = input(
        "What\'s your move: Rock, Paper, or Scissors: ").title()
    return user_choice


def get_winner(computer_choice, user_choice):
    if ((computer_choice == 'Rock') and (user_choice == 'Scissors')) or ((computer_choice == 'Scissors') and (user_choice == 'Paper')) or ((computer_choice == 'Paper') and (user_choice == 'Rock')):
        print("You lost")
    elif ((computer_choice == 'Paper') and (user_choice == 'Scissors')) or ((user_choice == 'Rock') and (computer_choice == 'Scissors')) or ((user_choice == 'Paper') and (computer_choice == 'Rock')):
        print("You won!")
    else:
        print("It is a tie!")

    return computer_choice, user_choice


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)


play()
