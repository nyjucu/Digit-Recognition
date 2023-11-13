# Digit-Recognition
Simple digit recognition application using a Keras model and the MNIST dataset.

## Installation
 import numpy as np
 
### import pandas as pd
-> the csv files are read using pandas

### from keras.models import Sequential 
### from keras.layers import Dense
-> keras models.Sequential and layers.Dense are used to build the neural network

from keras.utils import to_categorical
-> to_categorical function is used to one-hot the target label

from sklearn.model_selection import train_test_split
-> train_test_split function is used to split the dataset in testing and training features and labels
  
import time
-> used to get the running time of creating and compiling the model
  
import os
-> used to get rid of some tensorflow warnings
