#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Sat Dec 12 23:41:46 2020

@author: AdilFeroz
"""

import requests, base64
import json

keyapi='8f0cd00d5b49ffd8ece35b1e2c8c1062'
b64Val = base64.b64encode(keyapi.encode())
headers={"Authorization": "Basic %s" % str(b64Val.decode())}

                                                
url="https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
req_activity = requests.get(url,headers=headers )
jsonstr_activity=req_activity.text
new_json_activity=json.loads(jsonstr_activity)
print (new_json_activity)

url="https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
req_activity = requests.get(url,headers=headers )
jsonstr_activity=req_activity.text
new_json_activity=json.loads(jsonstr_activity)
print (new_json_activity)


url="https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
req_activity = requests.get(url,headers=headers )
jsonstr_activity=req_activity.text
new_json_activity=json.loads(jsonstr_activity)
print (new_json_activity)


url="https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
req_activity = requests.get(url,headers=headers )
jsonstr_activity=req_activity.text
new_json_activity=json.loads(jsonstr_activity)
print (new_json_activity)

