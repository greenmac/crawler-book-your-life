import requests
from pyquery import PyQuery as pq
import time
import socks
import socket
import os

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket

url = 'https://www.ptt.cc/bbs/ToS/index.html'
res = requests.get(url)
res_text = res.text
print(res_text)