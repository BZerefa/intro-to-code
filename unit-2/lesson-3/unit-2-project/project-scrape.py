import sys 
import requests 
from bs4 import BeautifulSoup 

if len(sys.argv) !=2:
   print("This program requires one argument; url of your choice to scrape")
   exit()

# Assign url_link variable to sys argument
url_link = sys.argv[1] 

# Use requests library to get information from link provided
website_response = requests.get(url_link) 

# Use beautifulsoup to parse through the site html
website_soup_html = BeautifulSoup(website_response.text, "html.parser") 

# Get the text from site html
website_soup_text = website_soup_html.get_text() 

# Add unicode utf8 to bypass UnicodeDecodeError
website_data = open('website.txt', 'w', encoding='utf-8') 
website_data.write(website_soup_text)
website_data.close()

def getTitles(soupdata):  
  # Changed h2 element to p element to get paragraphs in html
  paragraphs = soupdata.select("p") 
  if paragraphs:
    for p in paragraphs:
      print(p.text)