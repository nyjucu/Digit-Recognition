import numpy as np
import draw
from PIL import Image, ImageEnhance
from keras.models import load_model
from matplotlib import pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model = load_model("model.keras")

with Image.open("image_0.png") as image:
    # enhancer = ImageEnhance.Contrast(image)
    image = image.resize((28, 28))
    image = image.convert("L")

    X = np.array(image)
    X = (255 - X) / 255
    X = X.reshape((1, 784))

X *= 255
current_image = X.reshape((28, 28))
plt.gray()
plt.imshow(current_image, interpolation='nearest')
plt.show()

predicted_class = np.argmax(np.array(model.predict(X)))
print("Predicted Class:", predicted_class)
