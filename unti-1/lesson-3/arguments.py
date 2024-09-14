# arguments are bits of text to pass in programs to run (ex: cd is the command and argument is unit-1)
import sys

# a list in Python, which contains the command-line arguments passed to the script (sys. argv[0] , is the name of the script itself. Subsequent elements are the arguments passed to the script.)
print (sys.argv)

# print the length of the command line argument 
print(len(sys.argv))




# 
import sys 

# imputting data of numbers
data = [643, 452, 230, 219, 962, 532]

# vector of points given to the system, the integer assigned to it 
index = int(sys.argv[1])

#
print(data[index])




# check if the user did not enter an argument 
if len(sys.argv)<2:
    print("You forgot to type an argument")
    exit()

# error message if the user entered an argument that is too large
if len(sys.argv) < 2: 
    print("You typed a number that's too large") # can write anything in the quotations
    exit() # get out of the statement/stop running the program 


import sys 

# importing image object from pillow library 
from PIL import Image

# create new variable called whatever you want
img = Image.open(sys.argv[1])

# download 3 jpeg images into lesson-3 folder 
print("You typed the filename:" + sys.argv[1])
print("This is a " + img.format)
print(img.format_description)
print("Size:" +str(img.size))

# from the terminal: python3 arguments.py image-1.jpg 
