import cv2

image = cv2.imread(r'../images/cooked.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# гаусс
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

threshold1 = 90  # нп
threshold2 = 130  # вп

# обнаружения краев
edges = cv2.Canny(blurred, threshold1, threshold2)
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny Edges', cv2.WINDOW_NORMAL)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()