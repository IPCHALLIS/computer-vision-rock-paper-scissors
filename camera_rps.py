import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model("keras_Model.h5", compile=False)
cap = cv2.VideoCapture(0)
np.set_printoptions(suppress=True)
class_names = open("labels.txt", "r").readlines()

import random

labels = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    computer_choice = random.choice(labels)
    return computer_choice



def get_prediction():
    while cap.isOpened():
        end_after = 3
        start = time.time()
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(frame)
            normalized_image = (image_np.astype(np.float32) / 127.5) - 1 # Normalize the image
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            data[0] = normalized_image
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                while True:
                    timer = time.time() - start
                    prediction = model.predict(data)
                    index = np.argmax(prediction)
                    class_name = class_names[index]
                    confidence_score = prediction[0][index]
                    if timer >= end_after:
                        return class_name



# get_prediction()


def get_winner():
    computer_wins = 0
    user_wins = 0
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

    return computer_wins, user_wins

def play():
    rounds = 1
    while rounds <= 3:
        for i in range(rounds, 4):
            print()
            print("Press 's' key to start the countdown: " )
            print()
            print("Round: ", rounds)
            get_winner()
            rounds += 1
        else:
            break


play()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()