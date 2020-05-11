"""
============
Thresholding
============

Thresholding is used to create a binary image from a grayscale image [1]_.

.. [1] https://en.wikipedia.org/wiki/Thresholding_%28image_processing%29

.. seealso::
    A more comprehensive presentation on
    :ref:`sphx_glr_auto_examples_applications_plot_thresholding.py`

"""


import matplotlib.pyplot as plt
import skimage
from skimage import data
from skimage.filters import *
from skimage import io
import rasterio as rio
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


######################################################################
# We illustrate how to apply one of these thresholding algorithms.
# Otsu's method [2]_ calculates an "optimal" threshold (marked by a red line in the
# histogram below) by maximizing the variance between two classes of pixels,
# which are separated by the threshold. Equivalently, this threshold minimizes
# the intra-class variance.
#
# .. [2] https://en.wikipedia.org/wiki/Otsu's_method
#


image = io.imread("D:/HiWi/01_SALDI/Output_Mpumalanga/Driekoppies_VH_median_filter3_threshold_li7")
thresh = threshold_minimum(image, nbins=256, max_iter=1000)
binary = image < thresh

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 2, 1)
ax[1] = plt.subplot(1, 2, 2)

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

plt.show()

print("threshold of separation = " + str(thresh))

"""

print("Enter minimum dB value of raster scene:")
x = float(input())
print("Enter maximum dB value of raster scene:")
y = float(input())
difference = float(y - x)
quotient = float(difference/256)
threshold = thresh * float(quotient)
threshold_dB = str(threshold + x)
print("Threshold (in dB) = " + threshold_dB)
"""
"""
img = cv2.imread(r'D:\HiWi\01_SALDI\Output_Mpumalanga\subset_0_of_Driekoppies_VH_median_filter3_band_2.tif',0)
directory = r'D:\HiWi\01_SALDI\Output_Mpumalanga'
# Apply the binary threshold. The second parameter "150" can be adjusted here.
ret,thresh1 = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)

titles = ['Original Image','Binary: minimum (67)']
images = [img, thresh1]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

output_folder = 'D:/HiWi/01_SALDI/Output_Mpumalanga/'
filename = "savedImage.tif"
cv2.imwrite(output_folder + filename, thresh1)
print("After saving image:")
print(os.listdir(directory))

"""
######################################################################
# If you are not familiar with the details of the different algorithms and the
# underlying assumptions, it is often difficult to know which algorithm will give
# the best results. Therefore, Scikit-image includes a function to evaluate
# thresholding algorithms provided by the library. At a glance, you can select
# the best algorithm for your data without a deep understanding of their
# mechanisms.
#



#############################################################################################
#############################################################################################

"""

image = data.camera()

thresh = threshold_minimum(image, nbins=256, max_iter=1000)
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


######################################################################
# If you are not familiar with the details of the different algorithms and the
# underlying assumptions, it is often difficult to know which algorithm will give
# the best results. Therefore, Scikit-image includes a function to evaluate
# thresholding algorithms provided by the library. At a glance, you can select
# the best algorithm for your data without a deep understanding of their
# mechanisms.
#



from skimage.filters import try_all_threshold

img = data.page()

# Here, we specify a radius for local thresholding algorithms.
# If it is not specified, only global algorithms are called.
fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False)
plt.show()

"""
