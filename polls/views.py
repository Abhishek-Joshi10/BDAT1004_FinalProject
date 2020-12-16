import pandas as pd
import requests, base64
import json
from time import sleep
from rest_framework import viewsets
from .serializer import HeroSerializer
from .models import Product_Delhi

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Product_Delhi.objects.all().order_by('temp')
    serializer_class = HeroSerializer

keyapi='8f0cd00d5b49ffd8ece35b1e2c8c1062'
b64Val = base64.b64encode(keyapi.encode())
headers={"Authorization": "Basic %s" % str(b64Val.decode())}
from django.shortcuts import render
from .models import Product_Chennai, Product_Bangalore, Product_Delhi, Product_Hyderabad

# Create your views here.
from django.http import HttpResponse


def index(request):

    return render(request, 'welcome.html')


def getdata(request):
    try:
        # For Chennai
        url="https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
        req_activity = requests.get(url,headers=headers )
        jsonstr_activity=req_activity.text
        new_json_activity=json.loads(jsonstr_activity)
        Product_Chennai.objects.all().delete()
        sleep(2)
        row=Product_Chennai()
        sleep(2)
        row.temp=(new_json_activity['main']['temp'])
        sleep(2)
        row.feels_like=(new_json_activity['main']['feels_like'])
        sleep(2)
        row.temp_min=(new_json_activity['main']['temp_min'])
        sleep(2)
        row.temp_max=(new_json_activity['main']['temp_max'])
        sleep(2)
        row.save()
        sleep(2)

        # For Delhi
        url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
        req_activity = requests.get(url, headers=headers)
        jsonstr_activity = req_activity.text
        new_json_activity = json.loads(jsonstr_activity)
        Product_Delhi.objects.all().delete()
        sleep(2)
        row = Product_Delhi()
        sleep(2)
        row.temp = (new_json_activity['main']['temp'])
        sleep(2)
        row.feels_like = (new_json_activity['main']['feels_like'])
        sleep(2)
        row.temp_min = (new_json_activity['main']['temp_min'])
        sleep(2)
        row.temp_max = (new_json_activity['main']['temp_max'])
        sleep(2)
        row.save()
        sleep(2)

        #For Hyderabad
        url = "https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
        req_activity = requests.get(url, headers=headers)
        jsonstr_activity = req_activity.text
        new_json_activity = json.loads(jsonstr_activity)
        Product_Hyderabad.objects.all().delete()
        sleep(2)
        row = Product_Hyderabad()
        sleep(2)
        row.temp = (new_json_activity['main']['temp'])
        sleep(2)
        row.feels_like = (new_json_activity['main']['feels_like'])
        sleep(2)
        row.temp_min = (new_json_activity['main']['temp_min'])
        sleep(2)
        row.temp_max = (new_json_activity['main']['temp_max'])
        sleep(2)
        row.save()
        sleep(2)

        # for bangalore
        url = "https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=8f0cd00d5b49ffd8ece35b1e2c8c1062"
        req_activity = requests.get(url, headers=headers)
        jsonstr_activity = req_activity.text
        new_json_activity = json.loads(jsonstr_activity)
        Product_Bangalore.objects.all().delete()
        sleep(2)
        row = Product_Bangalore()
        sleep(2)
        row.temp = (new_json_activity['main']['temp'])
        sleep(2)
        row.feels_like = (new_json_activity['main']['feels_like'])
        sleep(2)
        row.temp_min = (new_json_activity['main']['temp_min'])
        sleep(2)
        row.temp_max = (new_json_activity['main']['temp_max'])
        sleep(2)
        row.save()
        sleep(2)

    except:
        print("Data has been fetched already")
    return HttpResponse('Data fetched succesfully go to /charts/')
    
def showcharts(request):
    # ModelName.objects.values('Colum_name') To get list of column

    c1 = Product_Chennai.objects.values('temp')
    c2 = Product_Chennai.objects.values('temp_min')
    c3 = Product_Chennai.objects.values('temp_max')
    c4 = Product_Chennai.objects.values('feels_like')
    d1 = Product_Delhi.objects.values('temp')
    d2 = Product_Delhi.objects.values('temp_min')
    d3 = Product_Delhi.objects.values('temp_max')
    d4 = Product_Delhi.objects.values('feels_like')
    h1 = Product_Hyderabad.objects.values('temp')
    h2 = Product_Hyderabad.objects.values('temp_min')
    h3 = Product_Hyderabad.objects.values('temp_max')
    h4 = Product_Hyderabad.objects.values('feels_like')
    b1 = Product_Bangalore.objects.values('temp')
    b2 = Product_Bangalore.objects.values('temp_min')
    b3 = Product_Bangalore.objects.values('temp_max')
    b4 = Product_Bangalore.objects.values('feels_like')

    return render(request,'charts.html',{'c1_data': float(c1[0]['temp']), 'c2_data': float(c2[0]['temp_min']), 'c3_data': float(c3[0]['temp_max']), 'c4_data': float(c4[0]['feels_like']), 'd1_data': float(d1[0]['temp']), 'd2_data': float(d2[0]['temp_min']), 'd3_data': float(d3[0]['temp_max']), 'd4_data': float(d4[0]['feels_like']), 'h1_data': float(h1[0]['temp']), 'h2_data':float(h2[0]['temp_min']), 'h3_data': float(h3[0]['temp_max']), 'h4_data': float(h4[0]['feels_like']), 'b1_data':float(b1[0]['temp']), 'b2_data':float(b2[0]['temp_min']), 'b3_data': float(b3[0]['temp_max']), 'b4_data': float(b4[0]['feels_like'])} )

