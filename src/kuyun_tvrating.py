#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
kuyun_tvrating
~~~~~~~~~~

This model return result file  as tv rate data from kuyun api

"""

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
urlminute = "http://eye.kuyun.com/api/min_ratings?tv_id=%s"

dictchannle={}
jsonchannle = json.loads(urllib.urlopen(urlchanel).read())
for item in jsonchannle["data"]:
    dictchannle[item["name"]] = item["id"]

fwrite = open("/home/asha/data/channetv","wb+")

for channel in dictchannle:
    tvraturl = urlminute % dictchannle[channel]
    try:
        jsontv = json.loads(urllib.urlopen(tvraturl).read())
    except Exception, e:
      raise e
    for tvrate in jsontv["data"]["list"]:
        req_params =[]
        for key,value in tvrate.items():
            if key !="timestamp" and key !="tv_ratings":
                key = "showname"
            req_params.append(key+"=" + str(value))
        fwrite.write(channel + "\t" + tvrate["timestamp"] + "\t" + "{".join(req_params) + "\n")


    