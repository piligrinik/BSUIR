import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

image = cv2.imread(r'../images/buildings.jpg')
original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def show_original():
    update_image(original_image)


def show_negative():
    negative_image = 255 - original_image
    update_image(negative_image)


def add_noise(value):
    value = float(value) * 0.01
    noisy = np.copy(original_image)
    salt_prob = value / 2
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape[:2]]
    noisy[coords[0], coords[1], :] = 255
    update_image(noisy)


def show_grayscale():
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)  # Для корректного отображения в RGB
    update_image(gray_image)


def show_sepia():
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image_3d = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_image = cv2.transform(gray_image_3d, sepia_filter)
    update_image(sepia_image)


def apply_median_filter(value):
    value = int(value)
    median_filtered_image = cv2.medianBlur(original_image, value)
    update_image(median_filtered_image)


def adjust_brightness(value):
    value = int(value)
    brightness_image = cv2.convertScaleAbs(original_image, alpha=1, beta=value)
    update_image(brightness_image)


def update_image(new_image):
    im = Image.fromarray(new_image)
    imgtk = ImageTk.PhotoImage(image=im)
    image_label.config(image=imgtk)
    image_label.image = imgtk


root = Tk()
root.title("Фильтры для изображений")
image_label = Label(root)
image_label.pack()

btn_original = Button(root, text="Оригинал", command=show_original)
btn_original.pack(side=LEFT)
btn_negative = Button(root, text="Негатив", command=show_negative)
btn_negative.pack(side=LEFT)
btn_grayscale = Button(root, text="Черно-белый", command=show_grayscale)
btn_grayscale.pack(side=LEFT)
btn_sepia = Button(root, text="Сепия", command=show_sepia)
btn_sepia.pack(side=LEFT)
brightness_slider = Scale(root, from_=-100, to=100, orient=HORIZONTAL, label="Яркость", command=adjust_brightness)
brightness_slider.pack(side=LEFT)
noise_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Шум", command=add_noise)
noise_slider.pack(side=LEFT)
median_slider = Scale(root, from_=0, to=20, orient=HORIZONTAL, label="Сглаживание", command=apply_median_filter)
median_slider.pack(side=LEFT)

show_original()

root.mainloop()


