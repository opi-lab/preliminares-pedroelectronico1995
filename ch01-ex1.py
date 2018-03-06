3# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:03:32 2018

@author: PEDRO NEL MENDOZA
 
Exercise 1: Take an image and apply Gaussian blur like in Figure 1-9. Plot the image contours
for increasing values of σ. What happens? Can you explain why?
""" 

# Firstly, the necessary libraries and modules are imported 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import filters 

# to read an image to array with the image converted to grayscale with convert('L')
perros = array(Image.open('data/perros.jpg').convert('L'))

# Show the image in grayscale:
plt.figure(figsize=(7,5))          # Figure size is defined.
plt.axis('off')                    # Axes are removed.
plt.imshow(perros,cmap='gray')
plt.show()                         # The image in grayscale is showed.

# Now, the image blurred contours for increasing values of σ are showed. 
i = 1;
plt.figure(figsize=(16,6))
for sigma in xrange (0,20,1):
    blurred_image = filters.gaussian_filter(perros, sigma)
    plt.subplot(4,5,i)
    plt.contour(blurred_image, origin='image',cmap='gray')
    plt.title('Image contour with sigma=%i' %sigma)
    plt.axis('off')
    i = i + 1;
plt.show()

'''
By tracing the contours of the blurred image by increasing the values 
of the standard deviation (sigma) and plotting these contours, it can 
be seen that as sigma increases, the image loses details, becoming 
increasingly blurred; in addition, the image vanishes, as if it were 
deteriorating with the increase of sigma In summary, it can be seen 
that blur affects the detection of contours; with more blurring 
(increasing sigma), fewer contours are detected, resulting in less
efficiency in contours detection.
'''