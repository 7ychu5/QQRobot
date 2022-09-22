from urllib.request import urlopen
import urllib.request
import requests
import json

async def get_yy():
    api = 'https://api.oddfar.com/yl/q.php?c=1007&'
    type = 'encode=json'
    url = api + type
    r = requests.get(url)
    jsons = json.loads(r.text)
    p = jsons['text']
    return p