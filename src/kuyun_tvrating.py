#! /usr/bin/env -python
# -*- coding:utf-8 -*-
import sys
import urllib
import json
import sys
from tqdm import tqdm
import time


reload(sys)
sys.setdefaultencoding('utf-8')


urltvlb = "http://eye.kuyun.com/api/tvlb"
urlchanel = "http://eye.kuyun.com/api/channel"
urlminute = "http://eye.kuyun.com/api/min_ratings?tv_id=5"
# 全部数据：
# http://eye.kuyun.com/api/tvlb
#  获取channel信息：
# http://eye.kuyun.com/api/channel
#  获取每小时节目信息：
# http://eye.kuyun.com/api/min_ratings?tv_id=5

# i = 0
# while True:
#     try:
#         data = urllib.urlopen(urltvlb).read()
#         jsondata = json.loads(data)
#         if jsondata['status']==True:
#             break
#         else: 
#             raise Exception("staus wrong")
#     except Exception, e:
#         raise e
#         if i <5:
#             i = i +1
#         else:
#             sys.exit(1)

dictchannle={}
jsonchannle = json.loads(urllib.urlopen("http://eye.kuyun.com/api/channel").read())
# print dictchannle
for item in jsonchannle["data"]:
  dictchannle[item["name"]] = item["id"]

fwrite = open("/home/asha/data/channetv","wb+")

for channel in dictchannle:
    tvraturl = "http://eye.kuyun.com/api/min_ratings?tv_id=%s" % dictchannle[channel]
    jsontv = json.loads(urllib.urlopen(tvraturl).read())
    for tvrate in jsontv["data"]["list"]:
        req_params =[]
        # fwrite.write(channel + "\t" + tvrate["timestamp"] + "\t" + json.dumps(tvrate).encode("utf8")  + tvrate[ tvrate["timestamp"]]+"\n")
        # print tvrate[ tvrate["timestamp"]]
        for key,value in tvrate.items():
            if key !="timestamp" and key !="tv_ratings":
                key = "showname"
            req_params.append(key+"=" + str(value))
        fwrite.write(channel + "\t" + tvrate["timestamp"] + "\t" + "{".join(req_params) + "\n")

# for item in jsondata['data']:
      # "tv_ratings": 0.00139,
      #       "market_ratings": 0.049339,
      #       "id": 9,
      #       "tv_name": "CCTV-4",
      #       "type": "央视",
      #       "epg_name": "远方的家",
      #       "rank": 4
    # print "\x02".join([str(item["id"]),item["tv_name"],item["type"],item["epg_name"],str(item["rank"]),str(float(item["tv_ratings"])),str(item["market_ratings"])])


    