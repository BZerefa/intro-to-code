import sys # importing system input output (i/o)
from PIL import Image # importing Image class (set of functions) from pillow

if len(sys.argv) !=3: # if length of system argument is not equal to 3 
    exit("This command requires two arguments: the name of an image file and degree to rotate") # exit program and display error message written

img = Image.open(sys.argv[1]) # open image through user input 
rotated_img=img.rotate(int(sys.argv[2])) # create a new variable to assign the rotate function output 
rotated_img.save("rotated-" + sys.argv[1]) # combining strings to become rotated-image-1.jpg