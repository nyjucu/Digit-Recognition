import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from keras.models import load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def make_prediction(index):
    pred_y = pred_df[0]
    pred_X = pred_df[1:]

    label = pred_y[index]
    prediction = np.argmax(model.predict(pred_X[:, index, None].T))
    # print(f"Prediction: {prediction}")
    # print(f"Label: {label}")

    current_image = pred_X[:, index, None]
    current_image = current_image.reshape((28, 28))
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    if label == 6:
        plt.show()


if __name__ == '__main__':
    model = load_model("model.keras")

    with open("digits.csv") as file:
        pred_df = pd.read_csv(file)

    pred_df = np.array(pred_df).T

    for i in range(10000):
        make_prediction(i)
