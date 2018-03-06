# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 21:12:08 2018

@author: PEDRO NEL MENDOZA
"""

# The module Image of PIL is imported:
from PIL import Image

mod_image = Image.open('data/torres_blancas.jpg') # Read an image 
mod_image.show()                             # Show the image

pil_image = Image.open('data/torres_blancas.jpg').convert('L') # Read an image and convert it to grayscale
pil_image.show()                            # Show the image in grayscale

# to create a thumbnail with longest side 150 pixels, use the method like this:
pil_image.thumbnail((150,150))
pil_image.show()        # Show the thumbnail image          

# to rotate the thumbnail image use counterclockwise angles and rotate(), in this case rotate(45): 
out = pil_image.rotate(45)
out.show()              # Show the thumbnail image rotated 45 degrees.

# Cropping a region from an image is done using the crop() method:
box1 = (100,100,300,300)        # Coordinates are (left, upper, right, lower)
region = mod_image.crop(box1)   # Crop a region from an image
region = region.transpose(Image.ROTATE_180)  # The extracted region is rotated 180 degrees.
mod_image.paste(region,box1)    # The region puts back using the paste() method    
mod_image.show()                # Show the region on the image

im = Image.open('data/perros.jpg').convert('L') # Read an image and convert it to grayscale
box3 = (200,200,400,400)        # Coordinates are (left, upper, right, lower)
region3 = im.crop(box3)         # Crop a region from an image
region3 = region3.transpose(Image.ROTATE_90) # The extracted region is rotated 90 degrees.
im.paste(region3,box3)          # The region puts back using the paste() method
im.show()                       # Show the region on the image

