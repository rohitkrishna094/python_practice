import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
img = cv2.imread('./lenna.png', cv2.IMREAD_GRAYSCALE)
rows = img.shape[0]
cols = img.shape[1]

new_img = np.empty((rows, cols), np.uint8)
# convert img into numpy
for x in range(rows):
    for y in range(cols):
        new_img[x, y] = img[x, y]

# define kernel
kernel = np.array([
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
])

conv_img = np.empty((rows - (kernel.shape[0]-1), cols - (kernel.shape[0]-1)), np.uint8)

convRows = conv_img.shape[0]
convCols = conv_img.shape[1]

# for x in convRows:
#     for y in

# display results
cv2.imshow('original image', new_img)
cv2.imshow('convoluted image', conv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
