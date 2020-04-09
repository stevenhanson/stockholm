import requests

from bs4 import BeautifulSoup

import pymysql

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36'}
movie_list = []
base_url = 'https://movie.douban.com/top250'


def get_html(url):
    res = requests.get(url, headers=headers)
    html = res.text
    return html


def parse_html(html):
    """
    解析html
    :param html:
    :return:
    """

    mysoup = BeautifulSoup(html, 'html.parser')
    movie_zone = mysoup.find('ol', attrs={'class': 'grid_view'})
    movie_li_list = movie_zone.find_all('li')

    for movie_li in movie_li_list:
        movie_name = movie_li.find('span', attrs={'class': 'title'}).getText()
        movie_list.append(movie_name)

    next_page = mysoup.find('span', attrs={'class': 'next'}).find('a')

    if next_page:
        new_url = base_url + next_page['href']
        parse_html(get_html(new_url))




def save_date(movie_list):
    pass


html = get_html(base_url)
parse_html(html)
print(movie_list)
