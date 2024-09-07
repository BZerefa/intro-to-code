# * = everything 
from unit1lesson2 import *

# () makes the function run
number_list.sort()
print(number_list[0]) # answer is 175

for x in number_list:
    if x > 500:
        print(x) # answer is 501
        break
        
# make a for loop to loop through the number list
for x in number_list:
# if x is even 
    if x%2 == 0:
        print(x) # answer is 176
        break

word_list.sort()
# alternative is print(word_list[-1]) where -1 is last on list
word_list.reverse()
print(word_list[0]) # answer is violation

# make a for loop to loop through the word list 
word_list.sort(key=len)
word_list.reverse()
print(word_list[0]) # answer is recommendation

# discuss formatting strings