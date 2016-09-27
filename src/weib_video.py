#-*-coding:utf8-*-

import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
from urllib import quote

reload(sys) 
sys.setdefaultencoding('utf-8')
# if(len(sys.argv)>=2):
#     user_id = (int)(sys.argv[1])
# else:
#     user_id = (int)(raw_input(u"请输入user_id: "))

cookie = {"Cookie": "_T_WM=b77b2d6ceb6675348a43753ed66c6f14; WEIBOCN_FROM=home; M_WEIBOCN_PARAMS=from%3Dhome%26uicode%3D20000173; SUB=_2A25627fdDeTxGeVM6FYV9CzNzziIHXVWJ9mVrDV6PUJbkdBeLWPxkW0XeqNBmM4u6esnedAw99fvKuGc7g..; SUHB=0pHxQiCH8WhaX5; SCF=ArckhK7M6sl9q1VJag3oC1kCU01O9DUWfMXBaMgi07tDLv4gOAgIi7EC5nDbKxG6FXz1z6J8XA0C7h9ImAUX31M.; SSOLoginState=1474283405"}
# cookie = {"Cookie":"SSOLoginState=1474341485; path=/; domain=.weibo.comSUB=_2A2565No9DeTxGeVM6FYV9CzNzziIHXVWJuZ1rDV8PUJbkNANLUWtkW0zv06P-N-V6mDivBZMuwtCZFXoXA..; Path=/; Domain=.weibo.com; Expires=Wed, 20 Sep 2017 03:18:05 GMT; HttpOnlySUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJx1NJ-pK__sAZkUTLiaI.5JpX5oz75NHD95Q0eoeXShBEeKBXWs4Dqcj.i--Xi-iWiK.pi--ci-zNi-2pi--RiKyWi-zpi--fiKy2i-zN; expires=Wednesday, 20-Sep-17 03:18:05 GMT; path=/; domain=.weibo.com"}
# url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id

keyword = "papi酱的周一放送——有些人是真不会聊天"
type =u'&smblog=%E6%90%9C%E5%BE%AE%E5%8D%9A'
url ="http://weibo.cn/search/?pos=search&keyword=%s" % quote(keyword)
# url ="http://weibo.cn/search/?keyword=%s" % quote(keyword)

print url

html = requests.get(url, cookies = cookie).content
print html
selector = etree.HTML(html)
pageNum = selector.xpath('//span[@class="ctt"]')
# pageNum = selector.xpath('//title/text()') 

print pageNum

print u'爬虫准备就绪...'

