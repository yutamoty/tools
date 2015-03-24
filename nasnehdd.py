#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import requests
import yaml
from pytweet import Twitter

conf = yaml.load(open('config.yaml'))

url = "http://%s:64210/status/HDDInfoGet?id=0" % conf['ipaddr']

r = requests.get(url)
hddinfo = r.json()

if hddinfo['errorcode'] == 0:
    usedb = hddinfo['HDD']['freeVolumeSize']
    usedgb = usedb / 1024 / 1024 /1024
else:
    sys.exit(1)

# 前回の発言と同一かチェック
hddinfotxt = open("hddinfo.txt", "r")
oldtxt = hddinfotxt.read()
hddinfotxt.close()

if int(oldtxt) != usedgb:
    text = u"@%s nasneの空き容量は %s GBです" % (conf['twitter_id'], usedgb)
    tw = Twitter(conf['consumer_key'], conf['consumer_secret'], conf['access_token'], conf['access_token_secret'])
    tw.tweet(text)
    hddinfotxt = open("hddinfo.txt", "w")
    hddinfotxt.write(str(usedgb))
    hddinfotxt.close()
    if __name__ == '__main__':
        print (text.encode("utf_8"))
else:
    sys.exit(0)
