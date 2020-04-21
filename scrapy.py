# utf-8 by myself
'''
import webbrowser,sys

import pyperclip

if len(sys.argv) >1 :
    address = "".join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://map.baidu.com/search/' + address)


import requests

res = requests.get('https://zhuanlan.zhihu.com/p/54430650')
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem :%s" %(exc))

type(res)
res.status_code = requests.codes.ok

playFile = open('zhihu.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()'''
# ! python3
# encoding=utf-8
# 遍历主页下边所有的url并下载所有图片

import requests, os, re
from bs4 import BeautifulSoup

url = 'https://www.doutula.com/article/detail/3828932'  # 遍历获取url
os.makedirs('斗图啦', exist_ok=True)
'''html = requests.get(url)
html.encoding = 'gb2312'''
'''infos = re.findall(r'a href="(https://www.doutula.com/article/detail/3828932.*?html)"  target="_blank" title="(.*?)" ',html.text)'''
'''src = re.search('<img src="(.*?)">',url) '''  # /i忽略大小写


def getpicurl(url):
    url = "https://www.doutula.com/article/detail/3828932"
    html = requests.get(url).text
    pic_url = re.findall('src="http://img.doutula.com/production/uploads/(.*?)"', html)
    for key in pic_url:
        print(key + "\r\n")
    print(pic_url)
getpicurl("https://www.doutula.com/article/detail/3828932")


while not url.endswith('#'):
    # Todo download the page
    print('Downloading page %s... ' % url)
    res = requests.get(getpicurl)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
# find photo image
photoElem = soup.select('#share-2')
# 遍历网页，寻找class下的src

if photoElem == []:
    print('Could not find photo image')
else:
    photoUrl = pic_url    # 遍历下来的src
    # download image
    print("Downloading image %s... " % (photoUrl))
    res = requests.get(photoUrl)
    res.raise_for_status()
    # save image
    imageFile = open(os.path.join("斗图啦", os.path.basename(photoUrl)), 'wb')
for chunk in res.iter_content(100000):  # 限制其消耗内存
    imageFile.write(chunk)
    imageFile.close()
print('Dnoe.')
