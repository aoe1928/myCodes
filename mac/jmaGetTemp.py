#！/usr/bin/env python 
# -*- coding: utf-8 -*-

import urllib.request as req
from bs4 import BeautifulSoup
import datetime

url = 'https://www.jma.go.jp/jp/amedas_h/today-44112.html'
# 八王子観測点
now_hour = datetime.datetime.now()
now_hour = now_hour.hour
if now_hour == 0:
    url = 'https://www.jma.go.jp/jp/amedas_h/yesterday-44112.html'
    now_hour = 24

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
block_middle = soup.find_all(class_="block middle")
res = block_middle[(now_hour-1) * 5].string

if res == '':
    res = block_middle[(now_hour-2) * 5].string
print(f'ただいまの気温は{res}度')
