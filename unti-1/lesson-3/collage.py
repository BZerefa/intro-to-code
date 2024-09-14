import sys 
from PIL import Image

if len(sys.argv) !=3: 
    exit("This command requires two filenames")

image1=Image.open(sys.argv[1]) 
image2=Image.open(sys.argv[2])
blended_image=Image.blend(image1, image2, 0.2)
blended_image.save("blended.jpg") # got Value:Error images do not match so adjusted width+height