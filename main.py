# Image segmentation is to modify the representation of an image into another
# representation that is easier to process.
# For example, image segmentation is commonly used to extract objects from
# the background based on some properties of the object (for example, color,
# edges, or histogram).

# What is Thresholding ?
# Thresholding is easiest form of Image Segmentation based on
# Intensity Value of Pixels.

# I GIobaI Thresholding  = whole image
# manual, Otsu, Triangle
# 2. Adaptive Thresholding = break image 
# Mean, Gaussian
# Niblack, Sauvola


import cv2

# Load the image
image = cv2.imread('Task_3.jpg', cv2.IMREAD_GRAYSCALE)

# Otsu's Thresholding
_, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('Task_3_otsu.jpg', otsu_threshold)

# Triangle Thresholding
_, triangle_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
cv2.imwrite('Task_3_triangle.jpg', triangle_threshold)

# Adaptive Thresholding 1
adaptive_threshold1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('Task_3_adaptive1.jpg', adaptive_threshold1)

# Adaptive Thresholding 2
adaptive_threshold2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('Task_3_adaptive2.jpg', adaptive_threshold2)
