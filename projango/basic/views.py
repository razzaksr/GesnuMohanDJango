import json
from django.shortcuts import render
from django.http import HttpResponse
from mongoengine import connect
from certifi import where

myCert=where()
client=connect(host="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority",
               db="forenoon",username="razak",password="mohamed",tlsCAFile=myCert)

# Create your views here.

from . import documents

def myReadOnly(req):
    obj = documents.Bike.objects.only('model','price','brand')
    for x in obj:
        print(x.to_json())
    return HttpResponse("Specific fields via only")

def myReadRequiring(req):
    obj = documents.Bike.objects.fields(model=1,year=1,cc=1)
    for x in obj:
        print(x.regno,x.model,x.brand,x.price,x.cc,x.year)
    return HttpResponse("Specific field done")

def myReadIgnoring(req):
    obj=documents.Bike.objects.exclude('regno')
    for x in obj:
        print(x.regno,x.model,x.brand,x.price,x.cc,x.year)
    return HttpResponse("Excluding specific field done")

def myRead(req,number):
    received=documents.Bike.objects(regno=number).first()
    print(received)
    return HttpResponse("Get One by reading regno done")
    

def myShow(req):
    myData=documents.Bike.objects.all()
    for x in myData:
        print(x)
    return HttpResponse("Printing all")
    

def myInsert(req):
    bike1=documents.Bike()#
    bike1._init__("TN54U9478","Ignis Sigma","Suzuki",2021,1988.9,612800)
    # bike1.model="Avenger Cruise"
    # bike1.brand="Bajaj"
    # bike1.cc=214.9
    # bike1.price=109800
    # bike1.year=2016
    # bike1.regno="TN54L4192"
    
    bike1.save()
    return HttpResponse("Bike is inserted")

def myBegin(req):
    collections=client['forenoon'].list_collection_names()
    for each in collections:
        print(each)
    return HttpResponse("hai there!!!!!!!!!!!!!!!!!")

