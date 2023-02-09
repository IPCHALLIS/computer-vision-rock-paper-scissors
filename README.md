# Computer Vision RPS

This repository is an interactive Rock, Paper, Scissors game that uses TensorFlow and Computer Vision to play with a user through a camera. I currently have four class labels: Rock, Paper, Scissors and Nothing. Each class contains over 600 image samples which have been recorded with the Teachable-Machine application.

For this model, I am currently using 105 epochs, 16 batches, and have a learning rate of 0.00146. The keras_model.h5 file contains the working model itself and the labels.txt file contains the four class labels the model is trained on.

## Virtual Environment Setup & The Game Code

So far, I have created a new virtual environment called rps_env using 'conda create -n (name)'. Initially, after trying to activate 'rps_env', I had the following warning report message from conda: "setuptools is replacing distutils". This prevented me from configuring my conda environment. I found the solution was to run 'pip install requests' as this seemed to be missing from the module list, hence, causing the problem. Afterwards, all issues were resolved and I could successfully install 'tensorflow', 'ipykernel' and 'opencv-python' to the environment.

Next, I cloned my 'computer-vision-rock-paper-scissors' repo from GitHub, and started writing the logic for a manual rock, paper, scissors game ('.py' file). Here I imported the random module, created a class labels list, and defined four functions.

The first function is called 'get_computer_choice'. This uses the 'random.choice' method, takes the class labels as an argument, and returns the choosen move.

The second function, 'get_user_choice', asks the user which move they wish to take, converts their input() to lower case and returns their choice.

The third function, 'get_winner', calls the previous two functions, assigns their output to 'computer' or 'user', respectively and returns the winner based on the 'classic rules' of the game. To implement this, I formulated if-elif-else conditions followed by a print statement.

Lastly, the fourth function, 'play', calls 'get_winner' to inherit all previous functions at once. When 'play' is called, the game will start.

## Milestone 5: Intergrating a keras model for the game with OpenCV

In this section, I created a new python file called camera_rps.py. Here, I replaced the hard-coded user input from the manual_rps.py file, with the output from the trained computer vision model ('keras_Model.h5'). To obtain the model's prediction, I used 'np.argmax(prediction)' which returns the index of the class label with the highest confidence score. For interpretability, I renamed this function to 'get_prediction', instead of 'get_user_choice'.

For the computer's choice, I used the same logic from the manual_rps.py file, i.e., random.choice(labels), returning a random class label from the list: ['Rock', 'Paper', 'Scissors'].

![Screenshot 2023-02-09 135922](https://user-images.githubusercontent.com/108879795/217833484-c37a8fa6-1ed2-4400-956d-769d4a6e7309.jpg)

From this point, I added the 'get_winner' function from the manual_rps.py file, for comparing the output of 'get_prediction' and 'get_computer_choice' functions respectively. However, to improve the performance, I added 3 rounds using a while-loop, meaning the user and computer's scores would accumulate towards the final round.

Next, I implemented a 3 second countdown timer for each round. To do this, I imported the time module and set it to start when the user presses the 's' key. I did this by specifying cv2.waitKey(1) & 0xFF == ord('s'), in the 'get_prediction' function. Once the user presses the 's' key, the game starts.

Lastly, I wanted to make my RPS game more interactive, so I decided to display the countdown timer in the webcam window using the 'cv2.putText' method. This way, the user can keep track of when they need to present their move to the camera so I can make a prediction in time.

Modules I used:

- random
- time
- cv2
- keras.models (load_model)
- numpy

## Areas for Improvement

1. The trained model is still very sensitive to light conditions, and hand distance from the webcam capture. It is sometimes difficult to get the model to read correct hand gesture despite training on over 250 images in each class. Perhaps, a hand tracking model would lend greater accuracy e.g., cvzone (object detection). However, I am confident that misclassification is not the result of imbalanced data, as I made sure each class was equally sampled.

2. I am aware that my 'get_winner' function has far too many if-elif-else statements, which is likely causing problems with code efficiency. I intend to improve this at some point in the future, although my main priority was getting the game to run initially. My reason for having multiple print statements was to adequately inform the user about the state of the game from within the terminal.

3. The countdown timer which is displayed in the webcam window is sometimes lagging, thus, can jump ahead to keep up in real-time. I think this has a lot to do with the computational complexity of the code itself. Hence, this may have some link to my previous point above.
