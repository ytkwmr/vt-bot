#coding:utf-8
import urllib
# f = urllib.urlopen("https://endpoints.office.com/version?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7")
f = urllib.urlopen('https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7')
res = f.read()
print(res) # <html>...


# import requests

# response = requests.get('https://endpoints.office.com/endpoints/worldwide')

# print(response.text)

# 'https://endpoints.office.com/version'
# 'https://endpoints.office.com/endpoints/worldwide'
# 'https://endpoints.office.com/changes/worldwide/0000000000'