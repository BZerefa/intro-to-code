import sys
from PIL import Image

# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")

# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 400x400, with a white background
# new_image = Image.new( "RGB", (400,400), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # paste in the second image, to (-200,200)
# new_image.paste(img2, (-200,200) )

# # save the resulting image
# new_image.save("overlay-two-images.jpg")

if len(sys.argv) != 3:
    exit("This program requires two arguments: the name of two image files to combine.")

# open both images
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

# resize both images so they are no bigger than 400x400
# but preserve the original aspect ratio
img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )

# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
new_image = Image.new( "RGBA", (400,260), "white" )

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (0,0) )

# add some transparency (alpha) to the second image
img2.putalpha(150)

# paste in the second image, preserving its new transparency
new_image.alpha_composite(img2, (0,0) )

# save the resulting image
# Note that we must convert it to RGB with no alpha to save it as a JPEG
new_image.convert("RGB").save("overlay-transparent.jpg")

# Alternatively, we could have avoided converting by saving it to a
# PNG like this (since PNGs allow alpha):
# new_image.save("overlay-transparent.png")