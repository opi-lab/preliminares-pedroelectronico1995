# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 20:36:59 2018

@author: PEDRO NEL MENDOZA
"""

# Firstly, the necessary libraries and modules are imported:
from PIL import Image
from numpy import *

im = array(Image.open('data/perros.jpg')) # Read an image to array
print im.shape, im.dtype # Print the shape of image array (rows, columns, color channels), and the data type of the array elements 
value = im[394,25,0]     # Value of the element of the row 394, column 25 and color channel 0
print(value)             # Print the previous value

im = array(Image.open('data/perros.jpg').convert('L'),'f') # It does grayscale conversion and creates the array with the extra argument “f”

# Important: The command "f" is for setting the type to floating point

print im.shape, im.dtype # Print the shape of image array (rows, columns) and the data type of the array elements

# Important: the grayscale image has only two values in the shape tuple; it has no color information (see the printout of the console)

print(im)               # Print the array im

im[0,:] = im[172,:] # Set the values of row 0 with values from row 172
print(im)           # Print the array im with the previous change (line 27)

im[:,2] = 100       # Set all values in column 2 to 100
print(im)           # Print the array im with the previous change (line 30)

suma1 = im[:10,:2].sum() # The sum of the values of the first 10 rows and 2 columns
print(suma1)             # Print the value of the sum

suma2 = im[:10,:3].sum() # The sum of the values of the first 10 rows and 3 columns
print(suma2)             # Print the value of the sum

media_fila_1= im[1].mean() # Average of row 1
print(media_fila_1)        # Print the value of average of row 1

print(im[-3,:])          # Print the third to last row
