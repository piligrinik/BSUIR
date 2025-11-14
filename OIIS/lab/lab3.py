import cv2
import numpy as np
import matplotlib.pyplot as plt


def equalize_color_image(image):
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
    equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
    return equalized_image

def plot_histogram(image, ax, title):
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y_channel = yuv_image[:, :, 0]
    y_channel_r = y_channel.ravel()
    ax.hist(y_channel.ravel(), bins=256, range=[0, 256], color='gray')
    ax.set_xlim([0, 256])
    ax.set_title(title)
    ax.set_xlabel('Яркость')
    ax.set_ylabel('Количество пикселей')

image1 = cv2.imread(r'../images/CanteDiMorte.jpg')
image2 = cv2.imread(r'../images/Donne.jpg')

equalized_image1 = equalize_color_image(image1)
equalized_image2 = equalize_color_image(image2)

#show
plt.figure(figsize=(22, 19))

# 1
plt.subplot(3, 4, 1)
plt.title('Оригинальное изображение 1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 2)
plt.title('Эквализованное изображение 1')
plt.imshow(cv2.cvtColor(equalized_image1, cv2.COLOR_BGR2RGB))
plt.axis('off')

# 2
plt.subplot(3, 4, 3)
plt.title('Оригинальное изображение 2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(3, 4, 4)
plt.title('Эквализованное изображение 2')
plt.imshow(cv2.cvtColor(equalized_image2, cv2.COLOR_BGR2RGB))
plt.axis('off')

ax1 = plt.subplot(3, 4, 5)
plot_histogram(image1, ax1, 'Гистограмма 1')

ax2 = plt.subplot(3, 4, 6)
plot_histogram(equalized_image1, ax2, 'Гистограмма 1 (после)')

ax3 = plt.subplot(3, 4, 7)
plot_histogram(image2, ax3, 'Гистограмма 2')

ax4 = plt.subplot(3, 4, 8)
plot_histogram(equalized_image2, ax4, 'Гистограмма 2 (после)')

# Показать все изображения и гистограммы

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()
