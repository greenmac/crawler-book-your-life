import requests
import random

"""
未使用代理
"""
# url = 'http://icanhazip.com'
# try:
#     response = requests.get(url) #不使用代理
#     print(response.status_code)
#     if response.status_code == 200:
#         print(response.text)
# except requests.ConnectionError as e:
#     print(e.args)

"""
使用代理
"""
proxies = [
    {'http':'socks5://127.0.0.1:1080'},
    # {'https':'socks5://127.0.0.1:1080'}
]
proxies = random.choice(proxies)
print(proxies)
url = 'http://icanhazip.com'
try:
    response = requests.get(url,proxies=proxies) #使用代理
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
except requests.ConnectionError as e:
    print(e.args)