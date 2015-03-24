#!/usr/bin/env python
#coding:utf-8

import sys
import yaml
from requests_oauthlib import OAuth1Session

class Twitter:
    def __init__(self, CK, CS, AT, AS):
        self.url = "https://api.twitter.com/1.1/statuses/update.json"
        self.CK = CK         # Consumer Key
        self.CS = CS         # Consumer Secret
        self.AT = AT         # Access Token
        self.AS = AS         # Accesss Token Secret

    def tweet(self, text):
        # ツイート本文
        params = {"status": text}
        # OAuth認証で POST method で投稿
        twitter = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        req = twitter.post(self.url, params = params)
        # レスポンスを確認
        if req.status_code == 200:
            print ("status OK")
        else:
            print ("status Error: %d" % req.status_code)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        conf = yaml.load(open('config.yaml'))
        tw = Twitter(conf['consumer_key'], conf['consumer_secret'], conf['access_token'], conf['access_token_secret'])
        tw.tweet(sys.argv[1])
        print (sys.argv[1])
    else:
        print ("%s [tweet word]") % sys.argv[0]
