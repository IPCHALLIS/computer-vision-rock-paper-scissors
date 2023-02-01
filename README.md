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