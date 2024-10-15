# list = ["I", "am", "so", "tired"]

# print(list)

# list.append("today") # append allows you to add things to a list

# print(list) 

# isSoInList = "so" in list # this line is asking if the string "so" is in list and giving that a variable

# print(isSoInList) # it prints true or false if the string is in list or not

### dictionary data structure
# key and value = word and definition 
mydic = {}
mydic["lover"] = "Bubby"
mydic["friends"] = ["Badah", "Car", "Ramneek", "Grace"]
mydic["family"] = ["Mommy", "Babi", "Fanuel", "Bisrat"]
mydic["siblings"] = ["Bisrat", "Fanuel"]

# checkForFriends = "friends" in mydic

# print(mydic)

# for key in mydic: 
#     print(key, ":", mydic[key])

mydic["total"] = 0

for key in mydic.items(): # .items is something you can call in the dictionary, can also call .value
    print(key)
    for x in key: # for loop through each key in dictionary
        if (type(x) is list): # check for if each key in dictionary is a list
            print("This is not a string, but there are", len(x), "items in this list!")

            for num in x: # for loop through the number of keys in dictionary
                mydic["total"] = mydic["total"] + 1 

        if (type(x) is str): 
            print("there are", len(x), "characters in this string:", x)

print(mydic)


# ### finish writing this code for assigment 
# from os import listdir, path
# from PIL import Image, ExifTags

# files = listdir("images") 
# img = Image.open(path.join("images", "0.jpg"))
# exifData = img.getexif()
