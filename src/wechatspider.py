#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import requests
from lxml import etree

import urllib
from bs4 import BeautifulSoup
from urllib import quote
import re 
p = re.compile("\d+")

baseurl="http://www.gsdata.cn/Query/article?q=%s&search_field=undefined&post_time=0&cp=0&range_title=1&range_content=1"
# eee = baseurl % quote("坏才刘克学")
# print eee
# # content = urllib.urlopen(baseurl %"布什家族").read()
# # time.sleep(10)
# # soup = BeautifulSoup(content,'lxml')
# # print soup.find('class="container-top"')

# dicresult = {}

html = requests.get(baseurl %"轩辕剑").content

selector = etree.HTML(html)
# content = selector.xpath('//h3[@class="container-top"]/a[1]/span')[0].text()
keylist = selector.xpath('//h3[@class="container-top"]/text()')
# print content
# #re.split(r'[\s\,]+', 'a,b, c  d')
# mykey = ["".join(re.split(r'[\s\n\r\t]+',key.replace("（","").replace("）",""))) for key in keylist]
content = selector.xpath('//h3[@class="container-top"]')[0]
wechatcount = content.findall('a/span')[0].text
articlecount = content.findall('span')[0].text
rankcount  =  content.findall('a/span')[1].text
readcount = content.findall('span')[1].text.strip()
# print re.findall(p,wechatcount)[0]
# print re.findall(p,articlecount)[0]
# print re.findall(p,rankcount)[0]
# print readcount
# print articlecount
# print rankcount
# print readcount
# print "\x03".join([wechatcount,articlecount,rankcount,readcount])

# sys.exit(1)

class WechatSpider(object):
    """docstring for WechatSpider"""
    def __init__(self, arg):
        super(WechatSpider, self).__init__()
        self.arg = arg
        self.keyfile = "/home/asha/project/weibo_crawler/keyfile"
        self.resultfile="/home/asha/project/weibo_crawler/output/wechats"
        self.baseurl="http://www.gsdata.cn/Query/article?q=%s&search_field=undefined&post_time=0&cp=0&range_title=1&range_content=1" 

    def readFile(self):
        with open(self.keyfile) as fread:
            for line in fread:
                aline = line.strip().replace('\n\r','')
                aimurl = self.baseurl % (aline)
                yield aline+"\x02"+aimurl
    def getData(self,aimurl):
        try:
            p = re.compile("\d+")
            headerst = {'User-Agent': "user-agent=Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}  
            html = requests.get(aimurl,headers=headerst).content
            # print html
            selector = etree.HTML(html)
            # print selector
            content = selector.xpath('//h3[@class="container-top"]')[0]
            # print content
            wechatcount = content.findall('a/span')[0].text
            articlecount = content.findall('span')[0].text
            rankcount  =  content.findall('a/span')[1].text
            readcount = content.findall('span')[1].text.strip()
            # print re.findall(p,wechatcount)[0]
            # print re.findall(p,articlecount)[0]
            # print re.findall(p,rankcount)[0]
            return "\x02".join([re.findall(p,wechatcount)[0],re.findall(p,articlecount)[0],re.findall(p,rankcount)[0],readcount])+"\n"
        except Exception, e:
            raise e

def main():
    if len(sys.argv) <2:
        print "usage: <date>"
        print "plz enter a date"
    else:
        datecol = sys.argv[1]
    
    headers = {'User-Agent': "user-agent=Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}  
    ws = WechatSpider(None)
    fwrite = open(ws.resultfile,"w+")
    for item in ws.readFile():
        keyname = item.split("\x02")[0]
        url = item.split("\x02")[1]
        resultvalue = ws.getData(url)
        fwrite.write(keyname+"\x02"+resultvalue)
        # time.sleep(30)
    fwrite.close()
if __name__ == '__main__':
    main()