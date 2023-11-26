# Digit-And-Letter-Recognition
Simple digit and letter recognition application using a Keras model and the MNIST dataset.


# About The Project
## Purpose 
The main purpose of this project is for the user to see the digit or the letter predicted by a neural network in real time. 
## Difficulty
This project is meant for begginer AI/ML programmers that want to solve their first image classification problem.

## Built With
Built in Python language using the Tensorflow framework.

### Downloading The MNIST Handwritten Digits Dataset
The digit recognision model is trained on the MNIST digits dataset. To download the dataset go tho the link below and follow the steps I provide.
Link to the MNIST dataset: kaggle.com/competitions/digit-recognizer/data
1. Scroll down and download the train.csv file
2. Copy it in the project file
3. Rename it to digits.csv

### Downloading the NIST Handwritten Letters Dataset
The letter recognision model is trained on the NIST letters dataset. To download the dataset go tho the link below and follow the steps I provide.
Link to the NIST dataset: https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format/data
1. Scroll down and download the A_Z Handwritten Data.csv file
2. Copy it in the project file
3. Rename it to letters.csv

### Installation of Packages
These can be done from the terminal or from the Python Packages section in PyCharm
Numpy
```
pip install numpy
```
Pandas 
```
pip install pandas
```
Keras 
```
pip install keras
```
Tensorflow 
```
pip install tensorflow
```
Sklearn
```
pip install scikit-learn
```

### Importing Packages
Numpy
```
import numpy as np
```
Pandas 
```
import pandas as pd
```
The csv files are read using pandas
Keras 
```
from keras.models import Sequential 
from keras.layers import Dense
```
Keras models.Sequential and layers.Dense are used to build the neural network
```
from keras.utils import to_categorical
```
Function to_categorical is used to one-hot the target label
Sklearn
```
from sklearn.model_selection import train_test_split
```
Function train_test_split is used to split the dataset in testing and training features and labels
Time 
```
import time
```
Used to get the running time of creating and compiling the model  
OS 
```
import os
```
Used to get rid of some tensorflow warnings

# Using the application
The UI is built entirely in the Tkinter library.

## Current File
To start the application run the main.py file. If you want to run the models (only after downloading the datasets) run the digit_model.py file and the letter_model.py file.

## The Widgets / Using the application
There are two white labels, one on the top of the window and one under it. The second one is only used to draw on it. The top one will show the resized image (from 350x450px to 28x28px) that the model uses to predict the digit.
The four buttons - BRUSH, ERASE, CLEAR, SAVE - do exactly what the name suggest.
The fifth button - DIGIT - is used to choose the model. If you want to predict a digit, leave it as is. If you want to predict a letter, press on it and its text will change to "LETTER".
The slider sets the size of the brush and the eraser.
