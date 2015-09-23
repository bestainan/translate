#-*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import json

string = input('中文:')

url = 'http://fanyi.baidu.com/v2transapi'
data = {}

data['from'] = 'en'
data['to'] = 'zh'
data['query'] = string
data['transtype'] = 'trans'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
htm = response.read().decode('utf-8')
htm = json.loads(htm)
end = htm["trans_result"]['data'][0]['result'][0][1]

print (end)
