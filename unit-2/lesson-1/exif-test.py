import sys
from os import listdir, path
from PIL import Image, ExifTags

img_name = sys.argv[1] # Made image name the first argument 
arg_after_img = sys.argv[2:] # Made an empty list of all arguments after image name

files = listdir("images") 
img = Image.open(path.join("images", img_name))
exifData = img.getexif()

if len(arg_after_img) == 0: # If there are no arguments after image name
    print("You have not provided any property code(s), input from following list: \n296 ResolutionUnit, \n34665 ExifOffset, \n271 Make, \n272 Model, \n305 Software, \n274 Orientation, \n306 DateTime, \n531 YCbCrPositioning, \n282 XResolution, \n283 YResolution, \n316 HostComputer")
    exit()

propery_codes = [296, 34665, 271, 272, 305, 274, 306, 531, 282, 283, 316] # Made a list of property codes

for property in arg_after_img: # For loop of property in argument(s) after image name
    int_property = int(property) # Converted property to integer 
    if int_property not in propery_codes:
        print("Invalid property code " + property + ", skipping...")
        continue

    print(exifData[int_property])

### Unit 2 Project idea in progress: Want it to be a question related to my thesis project for building a web archive of Ethiopian art and design, but not sure what specifically yet