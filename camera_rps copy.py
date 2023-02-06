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
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(frame)
            normalized_image = (image_np.astype(np.float32) / 127.5) - 1 # Normalize the image
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            data[0] = normalized_image
            cv2.imshow("Frame", frame)
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]
            print("Class:", class_name[:], end="")
            print("Confidence Score:", confidence_score)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return class_name
            break


#get_prediction()


def get_winner():
    computer = get_computer_choice()
    print(computer)
    user = get_prediction()
    print(user)
    if computer == 'Rock' and user == class_names[2]:
        print("You lost")
    elif computer == 'Paper' and user == class_names[2]:
        print("You won!")
    elif computer == 'Scissors' and user == class_names[1]:
        print("You lost")
    elif user == class_names[0] and computer == 'Scissors':
        print("You won!")
    elif user == class_names[1] and computer == 'Scissors':
        print("You lost")
    elif user == class_names[2] and computer == 'Paper':
        print("You won!")
    else:
        print("It is a tie!")

def play():
    get_winner()

play()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()