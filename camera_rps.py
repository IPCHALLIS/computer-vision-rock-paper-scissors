import random
import time
import cv2
from keras.models import load_model
import numpy as np


model = load_model("keras_Model.h5", compile=False)
cap = cv2.VideoCapture(0)
np.set_printoptions(suppress=True)
# reads class labels from this file
class_names = open("labels.txt", "r").readlines()


def get_computer_choice():
    """This function is for the computer to choose from the list of labels above.
    Returns:
        string: this could be "rock", "paper", or "scissors"
    """
    # list of class labels for function
    labels = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(labels)
    return computer_choice


def get_prediction():
    """This function opens and resizes the video capture.
        It waits for the user to press the 's' key.
        After the user presses 's', the timer counts to 3,
        and the model predicts if they chose 'rock', 'paper', or 'scissors'.

    Returns:
        string: prediction of the label is based on the index with the highest confidence value.
    """
    timer = 0  # timer starts at 0
    start = False  # when the game has not started yet
    result = False  # when the timer has not reached the limit

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(frame)
        normalized_image = (image_np.astype(np.float32) /
                            127.5) - 1  # Normalize the image
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image
        cv2.imshow('Frame', frame)

        if start:  # if start is true, game starts.
            if result is False:  # the result is not True when time is running
                timer = time.time() - initial_time
                font = cv2.FONT_HERSHEY_SIMPLEX  # used to display countdown timer in the webcam
                cv2.putText(frame, str(int(timer)), (50, 100),
                            font, 3, (0, 255, 255), 4, cv2.LINE_AA)
                # the model is predicting the image
                prediction = model.predict(data)
                # takes the label index of highest confidence
                index = np.argmax(prediction)
                # accesses the class name from 'labels.txt' file
                class_name = class_names[index]
                # returns class name during the countdown to see if the model is making accurate predictions or not.
                print("Class:", class_name[2:], end="")
                if timer > 3:  # if the timer exceeds 3 seconds;
                    result = True  # result becomes True and timer stops
                    return class_name  # returns the prediction class name

        cv2.imshow('Frame', frame)  # displays the webcam frame window

        key = cv2.waitKey(1)
        if key == ord('s'):  # game starts when the user presses the 's' key
            start = True  # after key is pressed, start is True;
            initial_time = time.time()  # timer is initiated


def get_the_winner():
    """This is used to compare the output from the computer's choice,
        and the model's predictions for the user.
        It will add points to the winner for each round out of 5.

    Returns:
        integer: this represents the number of points for the user or computer respectively
    """
    game_over = False
    rounds = 1  # rounds begin at 1
    computer_wins = 0  # variable to store computer wins
    user_wins = 0  # variable to store user wins

    while game_over is False:
        while rounds <= 5:  # function will repeat for total of 5 rounds
            if game_over is True:
                break
            for i in range(rounds, 6):
                print()
                print("Press 's' key to start the countdown: ")  # user prompt
                print()
                print("Round: ", rounds)  # shows the current round
                print()

                computer = get_computer_choice()
                user = get_prediction()

                # class_names[0] is 'Rock'
                # class_names[1] is 'Paper'
                # class_names[2] is 'Scissors'

                if ((computer == 'Rock') and (user == class_names[2])) or ((computer == 'Scissors') and (user == class_names[1])) or ((computer == 'Paper') and (user == class_names[0])):
                    print("You lost")
                    computer_wins += 1
                    print("Computer Chose: ", computer)
                    print("Your Score: ", user_wins)
                    print("Computer Score: ", computer_wins)

                elif ((computer == 'Paper') and (user == class_names[2])) or ((user == class_names[0]) and (computer == 'Scissors')) or ((user == class_names[1]) and (computer == 'Rock')):
                    print("You won!")
                    user_wins += 1
                    print("Computer Chose: ", computer)
                    print("Your Score: ", user_wins)
                    print("Computer Score: ", computer_wins)

                else:
                    print("It is a tie!")
                    print("Computer, also chose: ", computer)
                    computer_wins += 1
                    user_wins += 1
                    print("Your Score: ", user_wins)
                    print("Computer Score: ", computer_wins)

                if computer_wins == 3 and user_wins < 3:
                    print('The computer won the game overall!')
                    game_over = True
                    break
                elif user_wins == 3 and computer_wins < 3:
                    print('You won the game overall!')
                    game_over = True
                    break
                elif rounds > 3 and computer_wins > user_wins:
                    print('The computer won the game overall!')
                    game_over = True
                    break
                elif rounds > 3 and user_wins > computer_wins:
                    print('You won the game overall!')
                    game_over = True
                    break

                rounds += 1  # updates the round after each while loop

    return computer_wins, user_wins


def play_game():
    """This function is called in order to play the game.
    """
    get_the_winner()  # calls function above which inherits all previous functions


play_game()  # calls function

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
