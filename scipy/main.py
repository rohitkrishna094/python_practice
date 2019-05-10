import imageio
import skimage

# read an image as numpy array
img = imageio.imread('./assets/cat.jpg')
print(img.dtype, img.shape, img.ndim)

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
# img_tinted = img * [1, 0.95, 0.9]
img_tinted = img * [1, 0.7, 0.2]

# resize to be 300x300
# img_tinted = skimage.transform.resize(img_tinted, (300, 300))
imageio.imwrite('assets/cat_tinted.jpg', img_tinted)
