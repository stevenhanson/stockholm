
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Referer": "https://movie.douban.com/chart"
}

url = "https://movie.douban.com/cinema/nowplaying/changsha/"

response = requests.get(url, headers=headers)
text = response.text

# print(text)

html = etree.HTML(text)
ul = html.xpath("//div[@id='nowplaying']//ul[@class='lists']")[0]
print(ul)

lis = ul.xpath("./li")

for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    print(title, ":", score)
