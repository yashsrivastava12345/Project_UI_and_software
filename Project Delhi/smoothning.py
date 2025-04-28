import cv2
import numpy as np

# Load the image
img = cv2.imread("bgimg2.jpg", cv2.IMREAD_UNCHANGED)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary mask
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Optional: Morphological operations to remove small artifacts
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=1)

# Optional: Apply Gaussian Blur to soften jagged edges
blurred = cv2.GaussianBlur(cleaned, (5, 5), 0)

# Re-apply threshold after blur to keep edges crisp
_, final = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Convert back to 3-channel image for saving
output = cv2.cvtColor(final, cv2.COLOR_GRAY2BGR)

# Save the result
cv2.imwrite("inverted_image.jpg", output)
