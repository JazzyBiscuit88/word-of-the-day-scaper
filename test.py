import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup

#date header
today = date.today()
print(f"Article Of The Day for {today} is: ")

#url link
url = "https://en.wikipedia.org/wiki/Special:Random"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

#heading
heading = soup.find("h1", class_="firstHeading")
print(heading.text)

#body




