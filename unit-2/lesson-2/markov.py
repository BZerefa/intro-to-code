import markovify

text = open("website.txt").read()

generator = markovify.Text(text, state_size=3) # Changing state size (number of words the probability of a next word depends on)
# =20 None None None None None None None None None None

# =1 Of the collection of articles on the private collection of mutual trust. The encounters with their necks stretched forward as this conference trip. Correspondence with pile, of the diary. In this mask, were artfully decorated with his scholarly work. He also manuscripts and carving. Dabouzra Dah Dakar oder Binji Biombo Blale Blole? In African applied art. Therefore, such as well as a missionary. It was particularly elaborate. While he traveled regularly to Liberia Senegal oder zoologische.

# =3 None None The close cooperation, but also the acquisition of art objects. Together with his wife Ulrike. None None On the first trip, on the other hand also the sub-numbering within a collection. Together with his wife Ulrike. On the first trip, on the other hand also the sub-numbering within a collection. The close cooperation, but also the acquisition of art objects.

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")