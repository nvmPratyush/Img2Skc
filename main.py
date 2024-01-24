import cv2

# Load the image
image = cv2.imread("[your image].jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert = cv2.bitwise_not(gray)

# Apply Gaussian Blur to the inverted image
blur = cv2.GaussianBlur(invert, (21,21), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(blur)

# Create the sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# Save the resulting sketch
cv2.imwrite('[Your new sketch image file name].png', sketch)
