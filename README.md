# Digit-Recognition
Simple digit recognition application using a Keras model and the MNIST dataset.


# About The Project
## Purpose 
The main purpose of this project is for the user to see the digit predicted by a neural network in real time. 
## Difficulty
This project is meant for begginer AI/ML programmers that want to solve their first image classification problem.

## Built With
Built in Python language using the Tensorflow framework

### Downloading The MNIST Digits Dataset
The model is trained on the MNIST digits dataset. To download the dataset go tho the link below and follow the steps I provide.
Link to the MNIST dataset: kaggle.com/competitions/digit-recognizer/data
1. Scroll down and download the train.csv file
2. Copy it in the project file
3. Rename it to digits.csv

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
To start the application the current file needs to be draw.py. If you want to run the model (only if you download the MNIST digits dataset) the current file must be model.py

## The Widgets
There are two white labels, one on the top of the window and one under it. The top one will show the resized image (from 350x450px to 28x28px) that the model uses to predict the digit.
The four buttons - BRUSH, ERASE, CLEAR, SAVE - do exactly what the name suggest.
The slider sets the size of the brush and the eraser.
