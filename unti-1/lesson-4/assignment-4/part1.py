import sys
from PIL import Image

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         pixel = (x % 150, 100, y % 255)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        b = 0
        if x % 10 == 0:
            b = 255
            
        if y % 20 == 0:
            r = 255

        if y % 30 == 0:
            r = 255
            b = 100

        pixel = (r, 20, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])