from urllib.request import urlopen
import urllib.request
import requests
import json

async def get_pic():
    api = 'https://api.lolicon.app/setu/v2'
    type = '?type=json'
    url = api + type
    r = requests.get(url)
    jsons = json.loads(r.text)
    p = jsons['data'][0]['urls']['original']
    return p

async def get_pic_info():
    api = 'https://api.lolicon.app/setu/v2'
    type = '?type=json'
    url = api + type
    r = requests.get(url)
    jsons = json.loads(r.text)
    p = jsons['data'][0]['pid']
    return p