import requests

response = requests.get('https://www.baidu.com')
response.encoding='utf-8'

print(response.text)
print(response.headers)

# for attr in response:
#     print(attr)

resp = requests.get('http://t8.baidu.com/it/u=1484500186,1503043093&fm=79&app=86&f=JPEG?w=1280&h=853')

with open('phone.jpg', 'wb') as f:
    f.write(resp.content)



