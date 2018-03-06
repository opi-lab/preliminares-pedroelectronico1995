# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 21:41:33 2018

@author: PEDRO NEL MENDOZA
"""

# Firstly, the necessary libraries and modules are imported:
from PIL import Image
from pylab import *

oasis = array(Image.open('data/oasis.jpg')) # Read image to array
imshow(oasis) # Plot the image

# Some points (five points)
x = [90,300,400,90,410]
y = [300,350,210,300,300]

plot(x,y,'ko') # Plot the points with black circle-markers
plot(x[:4],y[:4],'g') # Green line plot connecting the first four points (the first point and the fourth point have the same ubication)

title('Plotting: "oasis.jpg"') # Add title to the plot
axis('off')                    # Axes are removed
show()                         # Starts the figure GUI and raises the figure windows

figure()                       # Create a new figure
hist(oasis.flatten(),10)       # Visualization of the image histogram with 10 bins
show()                         # Starts the figure GUI and raises the figure windows

figure()                       # Create a new figure
hist(oasis.flatten(),200)      # Visualization of the image histogram with 200 bins
show()                         # Starts the figure GUI and raises the figure windows