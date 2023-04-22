import requests
from bs4 import BeautifulSoup

url = "https://www.trbinance.com/markets"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

coin_etiketleri = soup.find_all("span", class_="w220-flex0-0-auto td4", attrs={"data-area": "left"})

for etiket in coin_etiketleri:
    coin_adi = etiket.text.strip()
    print(coin_adi)
