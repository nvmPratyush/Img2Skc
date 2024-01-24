import cv2

image = cv2.imread("Pratyush.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(gray)

blur = cv2.GaussianBlur(invert, (21,21),0)

inverted_blur = cv2.bitwise_not(blur)

skech = cv2.divide(gray, inverted_blur, scale=256.0)

cv2.imwrite('Pratyush_skech.png', skech)

