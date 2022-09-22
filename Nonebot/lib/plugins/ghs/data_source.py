from urllib.request import urlopen
import urllib.request
import requests
import json

async def get_pic(r):
    api = 'https://api.lolicon.app/setu/v2'
    type = '?type=json&size=regular'
    if r=="r18":
        type+="&r18=1"
    else:
        type+="&r18=0"
    url = api + type
    r = requests.get(url)
    jsons = json.loads(r.text)
    p = jsons['data'][0]
    return p
