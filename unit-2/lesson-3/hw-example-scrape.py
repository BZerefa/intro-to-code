import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://newyork.craigslist.org/search/zip#search=1~gallery~0~100")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

crgslist_data = open('crgslist_free.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()

freeStuff = []

def getTitles(soupdata):
    titles = soupdata.select(".title")
    if titles:
        for t in titles:
            freeStuff.append(t.get_text())

getTitles(crgslist_soup_html)
freeText = " ".join(freeStuff)

# crgslist_data = open('crgslist_free.txt', 'w')
# crgslist_data.write(freeText)
# crgslist_data.close()




# import requests
# from bs4 import BeautifulSoup

# cup_response = requests.get("https://welcometocup.org/projects/stories-data-power")

# cup_soup_html = BeautifulSoup(cup_response.text, "html.parser")

# cup_text = cup_soup_html.get_text()

# Data = []

# def getTitles(soupdata):
#     titles = soupdata.select(".title")
#     if titles:
#         for t in titles:
#             Data.append(t.get_text())

# getTitles(cup_soup_html)

# DataText = " ".join(Data)

# cup_data = open('crgslist_free.txt', 'w')
# cup_data.write(DataText)
# cup_data.close()