import markovify

# Use ./ to get into corpus folder and encoding utf8 to bypass unicode error
text = open("./corpus/all.txt", encoding="utf8").read() 

# Change state size (number of words the probability of a next word depends on)
generator = markovify.Text(text, state_size=2) 

paragraph = ""

# Print 25 randomly generated sentences of no more than 230 characters
for i in range(25):
    paragraph += str(generator.make_short_sentence(300)) 
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")