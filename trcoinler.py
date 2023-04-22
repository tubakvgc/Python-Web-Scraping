import requests
from bs4 import BeautifulSoup

url = "https://www.trbinance.com/markets"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

coin_etiketleri = soup.find_all('a', {'data-v-0cef6eb8': True, 'class': 'flex1'})

for etiket in coin_etiketleri:
    coin_adi = etiket.text.strip()
    print(coin_adi)
