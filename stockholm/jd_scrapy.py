"""
爬取京东商品信息
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Referer": "https://channel.jd.com/6196-6219.html"
}

url = "https://item.jd.com/1760966.html"

resp = requests.get(url, headers=headers)
html = resp.content.decode("gbk")

soup = BeautifulSoup(html, "lxml")
priceinf = soup.find("div", attrs={"class": "summary-price-wrap"})
dd = priceinf.find("div", attrs={"class": "dd"})
pprice = dd.find("span", attrs={"class": "p-price"})
price = pprice.find("span", attrs={"class": "J-p-1760966"})
print(price)
