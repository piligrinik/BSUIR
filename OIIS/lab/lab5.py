import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_images(left_image_path, right_image_path):
    # Загрузка изображений
    left_img = cv2.imread(left_image_path, cv2.IMREAD_GRAYSCALE)
    right_img = cv2.imread(right_image_path, cv2.IMREAD_GRAYSCALE)

    if left_img is None or right_img is None:
        raise ValueError("Не удалось загрузить одно из изображений")

    return left_img, right_img


def compute_disparity_map(left_img, right_img):
    # Инициализация алгоритма для вычисления карты диспаратности
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(left_img, right_img)

    # Нормализация карты диспаратности для отображения
    disparity_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
    disparity_normalized = np.uint8(disparity_normalized)

    return disparity_normalized


def display_stereo_image(left_img, right_img, disparity_img):
    # Отображение изображений
    plt.figure(figsize=(10, 7))

    plt.subplot(1, 3, 1)
    plt.imshow(left_img, cmap='gray')
    plt.title('Левое изображение')

    plt.subplot(1, 3, 2)
    plt.imshow(right_img, cmap='gray')
    plt.title('Правое изображение')

    plt.subplot(1, 3, 3)
    plt.imshow(disparity_img, cmap='hot')
    plt.title('Карта диспаратности')

    plt.show()


def main():
    # Пути к изображениям
    left_image_path = '../images/o1111.png'
    right_image_path = '../images/o2222.png'

    # Загрузка изображений
    left_img, right_img = load_images(left_image_path, right_image_path)

    # Вычисление карты диспаратности
    disparity_img = compute_disparity_map(left_img, right_img)

    # Отображение результатов
    display_stereo_image(left_img, right_img, disparity_img)


if __name__ == "__main__":
    main()