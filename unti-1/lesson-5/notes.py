# from PIL import Image
# import random # random is a library, which is a seperate set of code you can call on
# python3 (enter) import random (enter) random.random() to run on terminal
# int(random.random()*10) to get a number greater than decimals between zero and one
# 50+random.random()*50 to start from 50 instead of zero and go until 100 (multiply and extend range)
# random.randrange(0,50) does the same thing but faster
# random.seed(20), enter, random.random() to get same number/hold a random value


### pixel grid!
# imagePixels = [];
# width = 100
# height = 100
# for y in range(width):
#     for x in range(height): 
#         imagePixels.append((x,y))

# print(imagePixels, "\n \n \n There are", len(imagePixels), "pixels because the width multiplied by the height", width, "x", height, "is equal to", width*height) # slash n to add line break 





#### 3
### let's make a 100x100 black image

# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,0) )

# for y in range(height):
#     for x in range(width):    
#         # randomColorValue = random.randrange(255)
    
#         r = random.random()

#         if r > .9:
#             img.putpixel( (x,y), (240,255,255) )

# img = img.convert("RGB")
# randomnumberforimage = int(random.random()*20)
# img.save("so-less-random.png" + str(randomnumberforimage) + ".jpg")





# #### 4


# #### let's make a 100x100 white image

# width = 100
# height = 100

# img = Image.new("RGB", (width,height), (255,255,255) )

# # loop 500 times, and each time, pick a random x and a random y
# # and draw a pixel there
# for n in range(500):
    
#     ## even distribution
#     # x = int( random.random() * 100 )
#     # y = int( random.random() * 100 )

#     # ## gaussian distribution
#     # x = int( random.gauss(50,10) )
#     # y = int( random.gauss(50,10) )

#     ## gaussian distribution just for x
#     x = int( random.gauss(50,10) )
#     y = int( random.random() * 100  )

#     img.putpixel( (x,y), (0,0,0) )

# img.save("more-rando-gauss-x.png")



from os import listdir, path
import random
from PIL import Image

files = listdir("images")
# files.remove(".DS_Store")

random_file = random.choice(files)

img = Image.open( path.join("images",random_file) )



#5
# lyric = ['i','write','poems','on','my','computer']
# # random.seed(2)
# i = random.randrange( len(lyric) ) 
# aRandomWord = lyric[i]

# # aRandomWord = random.choice(lyric)

# print(aRandomWord)





## 6 in class exercise



# ### 7
# ##let's make a 100x100 white image

# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,255) )

# # ##loop 500 times, and each time, pick a random x and a random y
# # ## and draw a pixel there
# for n in range(500):

#     x = int( random.gauss(50,10) )
#     y = int( random.gauss(50,10) )

#     h = random.randrange(155,185)
#     s = random.randrange(235,255)
#     v = random.randrange(100,255)

#     img.putpixel( (x,y), (h,s,v) )

# img = img.convert(mode="RGB")
# img.save("rando-final.png")


