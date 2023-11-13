from tkinter import *
import PIL
import os
import numpy as np
import threading
import time
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageTk
from keras.models import load_model


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
TF_ENABLE_ONEDNN_OPTS = 0

model = load_model("model.keras")

lastx, lasty = None, None
image_number = 0
width = 10
predicted_class = 0


def save():
    global image_number
    filename = f'image_{image_number}.png'
    main_image.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def activate_erase(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', erase)
    lastx, lasty = e.x, e.y


def get_scale_value(val):
    global width
    width = int(val)


def clear_image():
    cv.delete("all")
    global main_image, draw
    main_image = PIL.Image.new('RGB', (350, 350), 'white')
    draw = ImageDraw.Draw(main_image)


def predict_image(image):
    global predicted_class, model_image

    image = image.resize((28, 28))
    image = image.convert("L")

    X = (255 - np.array(image)) / 255
    X = X.reshape((1, 784))

    predicted_class = np.argmax(np.array(model.predict(X)))
    class_label.config(text=str(predicted_class))

    # plt.gray()
    # plt.imshow(image, interpolation='nearest')
    # plt.show()

    model_image = image.resize((350, 350), Image.Resampling.NEAREST)


def paint(e):
    global lastx, lasty, model_image
    x, y = e.x, e.y
    offset = width / 2
    cv.create_line((lastx - offset, y, x + offset, y), width=width)
    draw.line((lastx - offset, y, x + offset, y), fill='black', width=width)
    lastx, lasty = x, y

    predict_image(main_image)

    model_image = ImageTk.PhotoImage(model_image)
    model_label.config(image=model_image)
    model_label.image = model_image


def erase(e):
    global lastx, lasty, model_image
    x, y = e.x, e.y
    offset = width / 2
    cv.create_line((lastx - offset, y, x + offset, y), fill='white', width=width)
    draw.line((lastx - offset, y, x + offset, y), fill='white', width=width)
    lastx, lasty = x, y

    predict_image(main_image)

    model_image = ImageTk.PhotoImage(model_image)
    model_label.config(image=model_image)
    model_label.image = model_image


root = Tk()

cv = Canvas(root, width=300, height=300, bg='white')
main_image = PIL.Image.new('RGB', (350, 350), 'white')
draw = ImageDraw.Draw(main_image)

model_image = PIL.Image.new('RGB', (350, 350), 'white')
model_image = ImageTk.PhotoImage(model_image)

model_label = Label(image=model_image)
model_label.pack()

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

class_label = Label(text="Predicted Digit")
class_label.pack()

btn_brush = Button(text="BRUSH", command=lambda: cv.bind('<1>', activate_paint), width=4, height=2, bg='black', fg='white')
btn_brush.pack(side=LEFT, padx=10, pady=10)

btn_erase = Button(text="ERASE", command=lambda: cv.bind('<1>', activate_erase), width=4, height=2, bg='white', fg='black')
btn_erase.pack(side=LEFT, padx=10, pady=10)

btn_save = Button(text="SAVE", command=save, width=5, height=2, bg='green', fg='white')
btn_save.pack(side=RIGHT, padx=10, pady=10)

btn_clear = Button(text="CLEAR", command=clear_image, width=4, height=2, bg='gray', fg='white')
btn_clear.pack(side=RIGHT, padx=10, pady=10)

sld_size = Scale(from_=10, to=60, orient=HORIZONTAL, command=get_scale_value)
sld_size.set(20)
sld_size.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
