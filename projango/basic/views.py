from django.shortcuts import render
from django.http import HttpResponse
from mongoengine import connect
from certifi import where

myCert=where()
client=connect(host="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority",
               db="forenoon",username="razak",password="mohamed",tlsCAFile=myCert)

# Create your views here.

from . import documents

# inc, dec, push, set

def myMobileCustomUp3(req):
    documents.Mobile.objects(model='c3').update_one(set__model='M2 Pro')
    return HttpResponse("C3 discontinued and expect m2 pro")

def myMobileCustomUp2(req):
    documents.Mobile.objects.update(push__features='smoke back case')
    return HttpResponse("Smoke case added to all mobiles")

def myMobileCustomUp(req):
    documents.Mobile.myOwnUpdate
    #documents.Mobile.objects(internal__gte=128).update(inc__internal=128)
    return HttpResponse("Updated by condition")

def myMobileArrange(req):
    for x in documents.Mobile.objects.order_by("-price"):
        print(x)
    return HttpResponse("Sorted by price")

def myMobileQuerysIn(req):
    for x in documents.Mobile.objects(features__in=['dolby atmos','dolby vision']):
        print(x)
    return HttpResponse("Filtered by dolby")

def myMobileQuerys(req):
    for x in documents.Mobile.objects(price__gte=10000):
        print(x)
    return HttpResponse("Filtered 10000 above")

def myMobileView(req):
    for x in documents.Mobile.objects.all():
        print(x)
    return HttpResponse("Mobile viewed")

def myDeletes(req):
    documents.Bike.moreDeleteByRegno
    return HttpResponse("TN54U9478 completly deleted")

def myDelete(req):
    received=documents.Bike.objects(regno="TN54U9478").first()
    received.delete()
    return HttpResponse("Document deleted")

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

