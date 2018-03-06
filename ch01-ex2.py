# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 00:12:17 2018

@author: PEDRO NEL MENDOZA

Exercise 2: Implement an unsharp masking operation (http://en.wikipedia.org/wiki/Unsharp_
masking) by blurring an image and then subtracting the blurred version from the
original. This gives a sharpening effect to the image. Try this on both color and
grayscale images.
"""

# Firstly, the necessary libraries and modules are imported
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters 

# to read an image to array:
oasis_color_rgb = np.array(Image.open('data/oasis.jpg'),'f')

# to read an image to array with the image converted to grayscale with convert('L'):
oasis_grayscale = np.array(Image.open('data/oasis.jpg').convert('L'),'f')

# FOR GRAYSCALE IMAGE

# Blurred image in grayscale:
blurred_image_gray = filters.gaussian_filter(oasis_grayscale, 5)

plt.figure(figsize=(10,6))
plt.subplot(231)
plt.imshow(oasis_grayscale,cmap='gray')
plt.title('Image in grayscale')
plt.axis('off')

# Details of image in grayscale:
details_image_gray = oasis_grayscale - blurred_image_gray
plt.subplot(232)
plt.imshow(details_image_gray,cmap='gray')
plt.title('Details of image in grayscale')
plt.axis('off')

peso = 0.6;
# Sharpened image in grayscale:
sharp_image_gray = oasis_grayscale + peso*details_image_gray
plt.subplot(233)
plt.imshow(sharp_image_gray,cmap='gray')
plt.title('Sharpened image in grayscale')
plt.axis('off')

plt.show()

# For COLOR IMAGE

alpha = 0.5;
sharpened_image_color = np.zeros(oasis_color_rgb.shape)
for i in range(3):
    # Blurred image to each color channel
    blurred_image_color = filters.gaussian_filter(oasis_color_rgb[:,:,i],5)
    
    # Details of image to each color channel
    details_channel_image_color = oasis_color_rgb[:,:,i] - blurred_image_color
    
    # Sharpened image to each color channel
    sharpened_image_color[:,:,i] = oasis_color_rgb[:,:,i] + alpha*details_channel_image_color
Im = sharpened_image_color-sharpened_image_color.min()
Im = Im/Im.max()*255

plt.figure(figsize=(10,6))

# Show image in color
plt.subplot(234)
plt.imshow(np.uint8(oasis_color_rgb))
plt.title('Image in color')
plt.axis('off')

# Show details of image in color
plt.subplot(235)
plt.imshow(details_channel_image_color,cmap='gray')
plt.title('Details of image in color')
plt.axis('off')

# Show sharpened image in color
plt.subplot(236)
plt.imshow(np.uint8(Im))
plt.title('Sharpened image in color')
plt.axis('off')

plt.show()