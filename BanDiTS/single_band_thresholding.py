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
import os

######################################################################
# We illustrate how to apply one of these thresholding algorithms.
# Otsu's method [2]_ calculates an "optimal" threshold (marked by a red line in the
# histogram below) by maximizing the variance between two classes of pixels,
# which are separated by the threshold. Equivalently, this threshold minimizes
# the intra-class variance.
#
# .. [2] https://en.wikipedia.org/wiki/Otsu's_method
#


image = io.imread("D:/HiWi/01_SALDI/Output_Mpumalanga/subset_0_of_Driekoppies_VH_median_filter3_band_2.tif")

thresh = threshold_minimum(image)
binary = image > thresh

print("threshold of separation = " + str(thresh))

plt.imshow(image)
plt.show()

print("Enter minimum dB value of raster scene:")
x = float(input())
print("Enter maximum dB value of raster scene:")
y = float(input())
difference = float(y - x)
quotient = float(difference/256)
threshold = thresh * float(quotient)
print("Threshold (in dB) = " + str(threshold + x))


"""
fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
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

"""
"""

from skimage.filters import try_all_threshold

img = data.page()

# Here, we specify a radius for local thresholding algorithms.
# If it is not specified, only global algorithms are called.
fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False)
plt.show()


"""

