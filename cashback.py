import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"}


for page in range(1, 7):
    url = f"https://cash-backer.club/shops?page={page}"

    allshop = soup.find("div", class_ ="shop-title")