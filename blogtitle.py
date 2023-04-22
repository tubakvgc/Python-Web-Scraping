import requests
from bs4 import BeautifulSoup

url = "https://www.trbinance.com/tr/blog/duyurular"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

duyuru_etiketleri = soup.select("h2.carousel-card-title.css-d9mrp4")

for etiket in duyuru_etiketleri:
    duyuru_baslik = etiket.text.strip()
    print(duyuru_baslik)
