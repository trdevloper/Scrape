
import requests
from bs4 import BeautifulSoup

url = "https://www.bch.org/Find-a-Physician/Search-Results.aspx"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

page = soup.find_all("span", {"class": "current-page"})

g_data = soup.find_all("div", {"class": "physician-item-detail flex"})
#z_data = soup.get_text("div", {"class": "physician-item-detail flex"})

a_data = soup.find_all("div",{"data-item":"i"})

for item in g_data:
    print (item.text)
