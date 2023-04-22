import requests
from bs4 import BeautifulSoup

url = "https://www.trbinance.com/markets"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

coin_etiketleri = soup.select("span.w110-flex110-1-0.td2")

for etiket in coin_etiketleri:
    coin_adi = etiket.text.strip()
    print(coin_adi)
