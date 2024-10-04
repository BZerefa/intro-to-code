import sys
from os import listdir, path 
import random
from PIL import Image, ImageDraw # imported ImageDraw from PIL

if len(sys.argv) !=5:
    print("This program requires four arguments; name of the image folder, resizing width, resizing height, and blend alpha")
    exit()

folder_name = sys.argv[1]
resizing_width = int(sys.argv[2])
resizing_height = int(sys.argv[3])
blend_alpha = float(sys.argv[4])

# randomly selecting two files from a folde(s) of multiple files
files = listdir(folder_name) 
random_file = random.choice(files)
random_file2 = random.choice(files)

# joining directory name and file name into the path to access files
img1 = Image.open(path.join(folder_name, random_file))
img2 = Image.open(path.join(folder_name, random_file2))

img1 = img1.resize((resizing_width,resizing_height)) 
img2 = img2.resize((resizing_width,resizing_height))
# (600,800) for folder1
# (736,1026) for folder2
# (900,1100) for folder3

blended_image=Image.blend(img1, img2, blend_alpha)
blended_imagedraw=ImageDraw.Draw(blended_image)

# randomly generated rectangle coordinates (x1,y1,x2,y2) within a range 
x1_color1 = int(random.randrange(100,400)) # x1 is how far you’d like to start from the left side
y1_color1 = int(random.randrange(200,500)) # y1 is how far you’d like to start from the top
x2_color1 = int(random.randrange(401,800)) # y2 is how far you’d like to go to the bottom
y2_color1 = int(random.randrange(501,900)) # y2 is how far you’d like to go to the bottom

x1_color2 = int(random.randrange(100,400))
y1_color2 = int(random.randrange(200,500))
x2_color2 = int(random.randrange(401,800))
y2_color2 = int(random.randrange(501,900))

# input randomized coordinate variables for color1 and color2
blended_imagedraw.rectangle((x1_color1,y1_color1,x2_color1,y2_color1), fill=None, outline="orange", width=3) 
blended_imagedraw.rectangle((x1_color2,y1_color2,x2_color2,y2_color2), fill=None, outline="red", width=3)
blended_image.save("blendeddraw.jpg") 