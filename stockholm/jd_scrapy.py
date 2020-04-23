"""
爬取京东商品
"""
import requests
from bs4 import BeautifulSoup
from urllib import parse
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}


GOODS_URL = "https://item.jd.com/1600815281.html#crumb-wrap"

BASE_STOCK_URL = "https://c0.3.cn/stock?area=18_1482_1485_0&venderId=31282&buyNum=1&choseSuitSkuIds=&cat=12259,12260," \
           "9435&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=2123370607&ch=1&callback=&skuId="


# 获取url对应的商品信息
def get_data(url):
    # params = parse.parse_qs(parse.urlparse(url).query)
    stockid = url[20:url.find(".html")]
    stock_url = BASE_STOCK_URL + stockid
    # print(stock_url)

    response = requests.get(stock_url, headers=headers)

    if response.status_code == 200:
        # print(response.text)
        return response.text

    # skuId = params["skuId"]


    pass


# 解析商品价格数据
def parse_value(text):
    jsondata = json.loads(text, encoding="gbk")
    print(jsondata)
    print(jsondata["stock"]["jdPrice"]["p"])


text = get_data(GOODS_URL)
parse_value(text)


# url = ""
#
# requests.get(url, headers=headers)