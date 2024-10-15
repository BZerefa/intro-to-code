import sys 
### Tried importing everything from file like in manovich bot practice but doesn't work on a non python file
    # from hamlet.txt import * 

f = open('hamlet.txt', 'r') # Opened text file for reading
hamlet = f.read() # Assigned variable to text file
# print(hamlet) # Printed content of text file

hamdic = {} # Created an empty dictionary

for line in hamlet.splitlines(): # Loop through each line in text file
    for word in line.split(): # Loop through each word in each line by splitting a string into a list 
        # print(word)
        uppercase_word = word.upper() # Make all words uppercase to avoid case sensitivity 
        if uppercase_word in hamdic:
            hamdic[uppercase_word] = hamdic[uppercase_word] + 1
        else: 
            hamdic[uppercase_word] = 1

sorted_keys = sorted(hamdic, key=hamdic.get)
sorted_keys.reverse()
# print(sorted_keys) # Top 10 most frequent words are 'the', 'and', 'of', 'to', 'I', 'in', 'my', 'it', 'a', 'not'

skip = ['THE', 'AND', 'TO', 'OF', 'IN', 'MY', 'A', 'IT', 'NOT', 'YOU', 'WITH', 'THAT', 'THIS', 'HIS', 'YOUR', 'OUR', 'BUT', 'IS', 'FOR', 'AS', 'HE', 'DO', 'BE', 'SO', 'HAVE', 'WE', 'WHAT', 'MOST', 'NO', 'BY']

filtered_words = []

for word in sorted_keys: # Iterate through sorted keys
    if word in skip: # Check if word exists in skip list
        continue # If it exists, continue
    else:
        filtered_words.append(word) # If it doesn't exist, add to list

print(filtered_words)

# Words with punctuation attached to them were counted multiple times and special characters are counted seperately, so would need to remove all special characters to get better outcome











# First attempt to print dictionary showed 'total = 0' repeatedly I think because I had assigned that value before the for loop

### Practiced split function to see how it works
    # txt = "hi my name is Beimnet"
    # x = txt.split()
    # print(x)