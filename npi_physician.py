
import requests
from bs4 import BeautifulSoup

url = "https://npiregistry.cms.hhs.gov/registry/search-results-table?city=BOULDER&state=CO"
url1 = "https://npiregistry.cms.hhs.gov/registry/search-results-table?city=BOULDER&state=CO&skip=100"
url2 = "https://npiregistry.cms.hhs.gov/registry/search-results-table?city=BOULDER&state=CO&skip=100&skip=200"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all("table", {"class": "table table-hover"})

for item in g_data:
    print (item.text)
