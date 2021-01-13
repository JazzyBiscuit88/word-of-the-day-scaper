import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup

#date header
today = date.today()
print(f"Word Of The Day for {today} is: ")

#url link
url = 'https://www.merriam-webster.com/word-of-the-day'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

#word-of-the-day
wotd = soup.findAll('h1')[0]

#class
word_class = soup.find("span", class_='main-attr')

#definitions
definitions = soup.select("div.wod-definition-container > p")


#did-you-know?
dyk = soup.find("div", class_='left-content-box')


print(wotd.text.upper(), "-", word_class.text)
print()
for el in definitions:
    print(el.text)
print(dyk.text)


