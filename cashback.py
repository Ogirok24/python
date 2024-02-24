import requests
import lxml
from bs4 import BeautifulSoup



class Cashback:
    def page(self):
        for page in range(1, 7):
            session = requests.Session()
            header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"}

            url = f"https://cash-backer.club/shops?page={page}"

            self.response = session.get(url, headers=header)
            self.soup = BeautifulSoup(self.response.text, "lxml")

            self.all_cashbacks = self.soup.find("div", class_="row col-lg-9 col-md-9 col-12")

            self.cashback = self.all_cashbacks.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")


    def texting(self):
            for elem in self.cashback:
                self.text = elem.find("div", class_="shop-title").text
                self.text1 = self.text[self.text.find(":")+1:self.text.find("%")]
                self.cashback_text = elem.find("div", class_="shop-rate").text
                self.cashback_text1 = self.cashback_text[self.cashback_text.find(":")++1:self.text.find("%")]
                with open("cashback.txt", "a", encoding="utf-8") as file:
                    file.write(f"{self.text} ---->>>> {self.cashback_text}\n")

cashback1 = Cashback()
cashback1.page()
cashback1.texting()
