import requests

import json

import datetime

import random

import string

import time

print ("Copy User ID From : Setting/Advanced/Diagnostics/ID")

print ("By - 6six6") 

referrer = input("WARP+ ID: ")

def genString(stringLength):

    letters = string.ascii_letters + string.digits

    return ''.join(random.choice(letters) for i in range(stringLength))


url = 'https://api.cloudflareclient.com/v0a745/reg'

def run():

    install_id = genString(11)

    body = {"key": "{}=".format(genString(42)),

            "install_id": install_id,

            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),

            "referrer": referrer,

            "warp_enabled": False,

            "tos": datetime.datetime.now().isoformat()[:-3] + "+08:00",

            "type": "Android",

            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',

               'Host': 'api.cloudflareclient.com',

               'Connection': 'Keep-Alive',

               'Accept-Encoding': 'gzip',

               'User-Agent': 'okhttp/3.12.1'

               }

    r = requests.post(url, data=bodyString, headers=headers)

    

    return r

c = 1

while True:

    result = run()

    if result.status_code == 200:

        print(c,"+1GB")

        c = c + 1

    else:

        time.sleep(1)
