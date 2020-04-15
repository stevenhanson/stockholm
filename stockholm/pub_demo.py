import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def parse_data(data):
    print(type(data))
    json_data = json.loads(data)
    posts = json_data['Data']['Posts']

    jobs = []

    for post in posts:
        job = {'name': post['RecruitPostName'], 'posturl': post['PostURL'], 'responsibility': post['Responsibility']}
        jobs.append(job)

    print(jobs)
    # soup = BeautifulSoup(html, 'lxml')

    # job_list = []
    # top_div = soup.find('div', attrs={'class': 'search-content'})
    # recruit_list = top_div.find_all('div', attrs={'class': 'recruit-list'})
    # for recruit in recruit_list:
    #     recruit_title = recruit.find('h4').get_text()
    #     recruit_text = recruit.find('p', attrs={'class': 'recruit-text'}).get_text()
    #     job = {'title': recruit_title, 'text': recruit_text}
    #     job_list.append(job)
    #
    # print(job_list)


def save_data():
    pass


if __name__ == '__main__':
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1585889938685&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
    html = get_data(url)
    parse_data(html)
