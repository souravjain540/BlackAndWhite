import imageio
import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np


def convert(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


img = "https://pbs.twimg.com/profile_images/1409095849032912897/mvDknRRy_400x400.jpg"
s = imageio.imread(img)
g = grayscale(s)
i = 255 - g
b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
r = convert(b, g)

# Saving the B&W picture
plt.imshow(r, cmap="gray")
plt.imsave('img2.png', r, cmap='gray', vmin=0, vmax=255)
