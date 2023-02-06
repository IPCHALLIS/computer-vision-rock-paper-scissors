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
                    print("Class:", class_name[:], end="")
                    if timer >= end_after:
                        return class_name
                        break


# get_prediction()


def get_winner():
    computer = get_computer_choice()
    user = get_prediction()
    print(user)
    if computer == 'Rock' and user == class_names[2]:
        print("You lost")
        print("Computer Chose: ", computer)
    elif computer == 'Paper' and user == class_names[2]:
        print("You won!")
        print("Computer Chose: ", computer)
    elif computer == 'Scissors' and user == class_names[1]:
        print("You lost")
        print("Computer Chose: ", computer)
    elif user == class_names[0] and computer == 'Scissors':
        print("You won!")
        print("Computer Chose: ", computer)
    elif user == class_names[1] and computer == 'Scissors':
        print("You lost")
        print("Computer Chose: ", computer)
    elif user == class_names[2] and computer == 'Paper':
        print("You won!")
        print("Computer Chose: ", computer)
    elif user == class_names[3]:
        print("You lost")
        print("You did not make a valid move!")
    else:
        print("It is a tie!")
        print("Computer, also chose: ", computer)

def play():
    get_winner()

play()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()