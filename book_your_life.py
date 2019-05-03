import requests
from pyquery import PyQuery as pq
import time
import socks
import socket
import os

# socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
# socket.socket = socks.socksocket

headers = {'Referer':'https://www.books.com.tw/',#如某些網站（如p站）要檢查referer，就給他加上
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'#每個爬蟲必備的偽裝
}

url = 'https://www.books.com.tw/'

mainPageDoc = requests.get(url, headers = headers)
mainPageDoc_text = mainPageDoc.text
mainPageDoc = pq(mainPageDoc_text)
mainPageDoc.make_links_absolute(base_url=url)
ranking_item_url = mainPageDoc('.style02 > h3 > a').attr('href')
# print(mainPageDoc_text)

ranking_item = requests.get(ranking_item_url)
ranking_item_text = ranking_item.text
ranking_item = pq(ranking_item_text)
ranking_item.make_links_absolute(base_url=ranking_item_url)
ranking_today_chinese_book_url = ranking_item('.type02_l001-1 > ul > li:nth-child(4) > span > a').attr('href')

ranking_today_chinese_book = requests.get(ranking_today_chinese_book_url)
ranking_today_chinese_book_text = ranking_today_chinese_book.text
ranking_today_chinese_book = pq(ranking_today_chinese_book_text)
ranking_today_chinese_book.make_links_absolute(base_url=ranking_today_chinese_book_url)
ranking_today_chinese_book_item = ranking_today_chinese_book('li.item').items()

i = 1
for ranking_today_chinese_book in ranking_today_chinese_book_item:
    rankingTodayChineseBookDict = {}
    rankingTodayChineseBookDict['rank'] = ranking_today_chinese_book('.no').text()
    rankingTodayChineseBookDict['title'] = ranking_today_chinese_book('.type02_bd-a > h4').text()
    rankingTodayChineseBookDict['url'] = ranking_today_chinese_book('.type02_bd-a > h4 > a').attr('href').replace(' ','')[:-15]
    """
    進入書的詳細介紹
    """    
    try:
        each_book_url = rankingTodayChineseBookDict['url']
        mainBook = requests.get(each_book_url)
        mainBook_text = mainBook.text
        mainBook = pq(mainBook_text)
        print(each_book_url)
        print(requests.get("http://icanhazip.com").text)
        print('===== ',i ,' =====')
        i += 1
        time.sleep(1)
        # os.system("killall -HUP tor")

    except Exception as e:
        print(str(e))
        continue
    else:
        continue

# ranking_today_chinese_book_item = ranking_today_chinese_book('.clearfix > ul > li:nth-child(1)')
# print(ranking_today_chinese_book_item('.type02_bd-a > h4 > a').attr('href'))
