import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка YOLO модели (конфигурация, веса)
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

image = cv2.imread('../images/oiis6.jpg')

teddy_image = cv2.imread('../images/teddy6.png')

height, width, channels = image.shape

blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# список для хранения информации
class_ids = []
confidences = []
boxes = []

confidence_threshold = 0.5
nms_threshold = 0.4

# обработка вых данных от YOLO
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > confidence_threshold:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = center_x - w // 2
            y = center_y - h // 2

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)


for i in range(len(boxes)):
    if i in indices:
        x, y, w, h = boxes[i]

        teddy_resized = cv2.resize(teddy_image, (w, h))

        # замена
        image[y:y + h, x:x + w] = teddy_resized
# вывод
cv2.imwrite('result_image_yolo.jpg', image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()