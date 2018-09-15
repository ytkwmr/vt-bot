#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import json
import urllib
import urllib2
 

# VirusTotalへhash値をリクエストし判定を返す関数
def vtinfo(apikey, hash):
	url = "https://www.virustotal.com/vtapi/v2/file/report"
	parameters = {"resource": hash, "apikey": apikey}
	 
	data = urllib.urlencode(parameters)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	json = response.read()
	print json


# コマンドライン引数から配列としてデータを取得しデータ数をカウント
argvs = sys.argv
argc = len(argvs)

if (argc != 2):
        print 'Usage: python %s hash' % argvs[0]
        sys.exit(1)
 
hash = argvs[1]

# 川村のAPIKey

apikey_list = [
	"97a8defe93052efcbc14dce54f74e5ece30d1ecfc94a7c765948cef35b3b92ba",
	"8d75816c394c50dcf6b43cab021471c1eed11bdcf786395e9753c2c96f7706ec",
	"c016ea3c60bee9774871fdeeb38e5f1f8ffb39a5f21fa45e2fb29c8c98af6327"
]

vtinfo(apikey_list[0], hash)