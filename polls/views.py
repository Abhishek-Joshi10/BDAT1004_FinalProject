import pandas as pd
import requests, base64
import json

keyapi='8f0cd00d5b49ffd8ece35b1e2c8c1062'
b64Val = base64.b64encode(keyapi.encode())
headers={"Authorization": "Basic %s" % str(b64Val.decode())}
from django.shortcuts import render
from .models import Product_Chennai, Product_Bangalore, Product_Delhi, Product_Hyderabad

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def getdata():
       
                                     
    url="https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
    req_activity = requests.get(url,headers=headers )
    jsonstr_activity=req_activity.text
    new_json_activity=json.loads(jsonstr_activity)
    # For Chennai
    Product_Chennai.objects.all().delete()
    row=Product_Chennai()
    row.temp=(new_json_activity['main']['temp'])
    row.feels_like=(new_json_activity['main']['feels_like'])
    row.temp_min=(new_json_activity['main']['temp_min'])
    row.temp_max=(new_json_activity['main']['temp_max'])
    row.save()
    # For Delhi
    url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
    req_activity = requests.get(url, headers=headers)
    jsonstr_activity = req_activity.text
    new_json_activity = json.loads(jsonstr_activity)
    Product_Delhi.objects.all().delete()
    row = Product_Delhi()
    row.temp = (new_json_activity['main']['temp'])
    row.feels_like = (new_json_activity['main']['feels_like'])
    row.temp_min = (new_json_activity['main']['temp_min'])
    row.temp_max = (new_json_activity['main']['temp_max'])
    row.save()

    #For Hyderabad
    url = "https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
    req_activity = requests.get(url, headers=headers)
    jsonstr_activity = req_activity.text
    new_json_activity = json.loads(jsonstr_activity)
    Product_Hyderabad.objects.all().delete()
    row = Product_Hyderabad()
    row.temp = (new_json_activity['main']['temp'])
    row.feels_like = (new_json_activity['main']['feels_like'])
    row.temp_min = (new_json_activity['main']['temp_min'])
    row.temp_max = (new_json_activity['main']['temp_max'])
    row.save()

    # for bangalore
    url = "https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
    req_activity = requests.get(url, headers=headers)
    jsonstr_activity = req_activity.text
    new_json_activity = json.loads(jsonstr_activity)
    Product_Bangalore.objects.all().delete()
    row = Product_Bangalore()
    row.temp = (new_json_activity['main']['temp'])
    row.feels_like = (new_json_activity['main']['feels_like'])
    row.temp_min = (new_json_activity['main']['temp_min'])
    row.temp_max = (new_json_activity['main']['temp_max'])
    row.save()
    return HttpResponse('My website')
    
def showcharts(request):
    # ModelName.objects.values('Colum_name') To get list of column
    getdata()
    c1 = Product_Chennai.objects.values('temp')
    c2 = Product_Chennai.objects.values('temp_min')
    d1 = Product_Delhi.objects.values('temp')
    d2 = Product_Delhi.objects.values('temp_min')
    h1 = Product_Hyderabad.objects.values('temp')
    h2 = Product_Hyderabad.objects.values('temp_min')
    b1 = Product_Bangalore.objects.values('temp')
    b2 = Product_Bangalore.objects.values('temp_min')

    return render(request,'charts.html',{'c1_data': float(c1[0]['temp']), 'c2_data': float(c2[0]['temp_min']), 'd1_data': float(d1[0]['temp']), 'd2_data': float(d2[0]['temp_min']), 'h1_data': float(h1[0]['temp']), 'h2_data':float(h2[0]['temp_min']), 'b1_data':float(b1[0]['temp']), 'b2_data':float(b2[0]['temp_min'])} )

