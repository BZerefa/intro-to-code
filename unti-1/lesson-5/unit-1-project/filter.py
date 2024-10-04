import sys
from os import listdir, path 
import random
from PIL import Image, ImageFilter # imported ImageFilter from PIL

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
img1 = Image.open( path.join (folder_name, random_file))
img2 = Image.open( path.join (folder_name, random_file2))

img1 = img1.resize((resizing_width,resizing_height)) 
img2 = img2.resize((resizing_width,resizing_height))
# (600,800) for folder1
# (736,1026) for folder2
# (900,1100) for folder3

blended_image=Image.blend(img1, img2, blend_alpha)
blended_image=blended_image.filter(ImageFilter.EMBOSS) # changing filter to emboss, contour, detail, or enhance
blended_image.save("blendedfilter.jpg")