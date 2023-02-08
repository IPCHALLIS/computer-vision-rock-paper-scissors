import random
import time
import cv2
from keras.models import load_model
import numpy as np


model = load_model("keras_Model.h5", compile=False)
cap = cv2.VideoCapture(0)
np.set_printoptions(suppress=True)
class_names = open("labels.txt", "r").readlines()


labels = ['Rock', 'Paper', 'Scissors']


def get_computer_choice():
    """This function is for the computer to choose from the list of labels above.
    Returns:
        string: this could be "rock", "paper", or "scissors"
    """
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
    timer = 0
    start = False
    result = False

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(frame)
        normalized_image = (image_np.astype(np.float32) /
                            127.5) - 1  # Normalize the image
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image
        cv2.imshow('Frame', frame)

        if start:
            if result is False:
                timer = time.time() - initial_time
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(int(timer)), (50, 100),
                            font, 3, (0, 255, 255), 4, cv2.LINE_AA)
                prediction = model.predict(data)
                index = np.argmax(prediction)
                class_name = class_names[index]
                if timer > 3:
                    result = True
                    return class_name

        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            start = True
            initial_time = time.time()


# get_prediction()


def get_winner():
    """This is used to compare the output from the computer's choice,
        and the model's predictions for the user.
        It will add points to the winner for each round out of 3.

    Returns:
        integer: this represents the number of points for the user or computer respectively
    """
    rounds = 1
    computer_wins = 0
    user_wins = 0
    while rounds <= 3:
        for i in range(rounds, 4):
            print()
            print("Press 's' key to start the countdown: ")
            print()
            print("Round: ", rounds)
            print()
            computer = get_computer_choice()
            user = get_prediction()
            if computer == 'Rock' and user == class_names[2]:
                print("You lost")
                print("Computer Chose: ", computer)
                computer_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif computer == 'Paper' and user == class_names[2]:
                print("You won!")
                print("Computer Chose: ", computer)
                user_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif computer == 'Scissors' and user == class_names[1]:
                print("You lost")
                print("Computer Chose: ", computer)
                computer_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif user == class_names[0] and computer == 'Scissors':
                print("You won!")
                print("Computer Chose: ", computer)
                user_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif user == class_names[1] and computer == 'Scissors':
                print("You lost")
                print("Computer Chose: ", computer)
                computer_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif user == class_names[2] and computer == 'Paper':
                print("You won!")
                print("Computer Chose: ", computer)
                user_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            elif user == class_names[3]:
                print("You lost")
                print("You did not make a valid move!")
                computer_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            else:
                print("It is a tie!")
                print("Computer, also chose: ", computer)
                computer_wins += 1
                user_wins += 1
                print("Computer Score: ", computer_wins)
                print("Your Score: ", user_wins)
            rounds += 1
        else:
            break

    return computer_wins, user_wins


def play():
    """This function is called in order to play the game.
    """
    get_winner()


play()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
