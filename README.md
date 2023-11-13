# Digit-Recognition
Simple digit recognition application using a Keras model and the MNIST dataset.

## Installation
### Numpy
```
import numpy as np
```
### Pandas 
```
import pandas as pd
```
The csv files are read using pandas
### Keras 
```
from keras.models import Sequential 
from keras.layers import Dense
```
Keras models.Sequential and layers.Dense are used to build the neural network
```
from keras.utils import to_categorical
```
to_categorical function is used to one-hot the target label
### Sklearn
```
from sklearn.model_selection import train_test_split
```
train_test_split function is used to split the dataset in testing and training features and labels
### Time 
```
import time
```
used to get the running time of creating and compiling the model  
### OS 
```
import os
```
used to get rid of some tensorflow warnings
