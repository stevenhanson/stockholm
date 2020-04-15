import time

import requests

from bs4 import BeautifulSoup

import pymysql

import pandas as pd

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
        time.sleep(1)
        new_url = base_url + next_page['href']
        parse_html(get_html(new_url))


def save_date(movie_list):
    conn = pymysql.connect(host='localhost', user='root', password='123456789', db='test')
    mycursor = conn.cursor()
    # sql = 'CREATE TABLE movie250(ID VARCHAR(10), NAME VARCHAR(100)) DEFAULT CHARSET = utf8'
    # mycursor.execute(sql)

    for id, movie in enumerate(movie_list):
        sql = "INSERT INTO movie250 VALUES(%s, %s)"
        mycursor.execute(sql, (id, movie))

    conn.commit()
    mycursor.close()
    conn.close()


html = get_html(base_url)
parse_html(html)
# print(movie_list)
save_date(movie_list)
# df = pd.DataFrame(movie_list)
# print(df)
