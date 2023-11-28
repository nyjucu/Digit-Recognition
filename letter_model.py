import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == '__main__':
    start_time = time.time()

    with open("letters.csv") as file:
        df = pd.read_csv(file)

    df = np.array(df).T
    m, n = df.shape

    y = to_categorical(df[0], 26)
    X = df[1:].T / 255

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # X_train (33600, 784)
    # y_train (33600, 10)

    # X_test (8400, 784)
    # y_test (8400, 10)

    model = Sequential()
    model.add(Dense(1024, input_shape=(784,), activation='relu', name='hidden_layer_1'))
    model.add(Dense(512, activation='relu', name='hidden_layer_2'))
    model.add(Dense(512, activation='relu', name='hidden_layer_3'))
    model.add(Dense(26, activation='softmax', name='output_layer'))

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

    print("Model created...")

    model.fit(X_train, y_train, epochs=16, batch_size=512, verbose=1)

    _, accuracy = model.evaluate(X_test, y_test)

    print(f"Accuracy of model: {accuracy}")
    print(f"Time to run: {time.time() - start_time}")

    model.save("letter_model.keras")
    print("Model saved...")

    # Final accuracy of approx. 99.2%
