
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import data
from skimage.filters import *
from skimage import io
import rasterio as rio
import os


# Read the geotiff as greyscale image
"""
img = cv2.imread(r'D:\HiWi\01_SALDI\Output_Mpumalanga\subset_0_of_Driekoppies_VH_median_filter3_band_2.tif',0)

# Apply the binary threshold. The second parameter "150" can be adjusted here.
ret,thresh1 = cv2.threshold(img,67,255,cv2.THRESH_BINARY)

titles = ['Original Image','Binary']
images = [img, thresh1]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
"""


image = data.camera()

thresh = threshold_triangle(image)
# thresh = threshold_li(image)
# thresh = threshold_yen(image)
# thresh = threshold_otsu(image)
# thresh = threshold_minimum(image)
# thresh = threshold_mean(image)
binary = image < thresh




fig, axes = plt.subplots(ncols=3, figsize=(15, 5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()

