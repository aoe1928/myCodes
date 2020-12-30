#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://www.data.jma.go.jp/obd/stats/etrn/select/prefecture00.php?prec_no=&block_no=&year=&month=&day=&view='
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

print(soup)