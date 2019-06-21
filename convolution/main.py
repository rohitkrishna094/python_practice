import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.exposure import rescale_intensity


def convolveSingle(kernel, arr):
    return np.sum(kernel * arr)


def convolve_mine(img, kernel):
    output = np.empty((img.shape[0] - (kernel.shape[0]-1), img.shape[1] - (kernel.shape[0]-1)), np.uint8)
    convRows = output.shape[0]
    convCols = output.shape[1]

    for y in range(convCols):
        for x in range(convRows):
            output[x, y] = convolveSingle(kernel, img[x: x + kernel.shape[0], y: y + kernel.shape[1]])
    return output


def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            k = (roi * kernel).sum()

            output[y - pad, x - pad] = k

    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


# read image
img = cv2.imread('./lenna.png', cv2.IMREAD_GRAYSCALE)

# define kernel
identityKernel = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

edgeKernel1 = np.array([
    [1, 0, -1],
    [0, 0, 0],
    [-1, 0, 1]
])

edgeKernel2 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

edgeKernel3 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

sharpenKernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

boxBlurKernel = (1 / 9) * np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

gaussianBlurKernel1 = (1 / 16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

gaussianBlurKernel2 = (1 / 256) * np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])

unsharpMaskingKernel = (-1 / 256) * np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, -476, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])


listOfOutputs = {
    'identity': convolve(img, identityKernel),
    'edgeKernel1': convolve(img, edgeKernel1),
    'edgeKernel2': convolve(img, edgeKernel2),
    'edgeKernel3': convolve(img, edgeKernel3),
    'sharpenKernel': convolve(img, sharpenKernel),
    'boxBlurKernel': convolve(img, boxBlurKernel),
    'gaussianBlurKernel1': convolve(img, gaussianBlurKernel1),
    'gaussianBlurKernel2': convolve(img, gaussianBlurKernel2),
    'unsharpMaskingKernel': convolve(img, unsharpMaskingKernel),
}

# display results
cv2.imshow('original image', img)

for kernelName, outputImage in listOfOutputs.items():
    cv2.imshow(kernelName, outputImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
