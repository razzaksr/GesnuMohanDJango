from mongoengine import *
from certifi import where

myCert=where()
client=connect(host="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority",
               db="forenoon",username="razak",password="mohamed",tlsCAFile=myCert)

class Mobile(Document):
    brand=StringField()
    features=ListField()
    model=StringField()
    price=IntField()
    ram=IntField()
    internal=IntField()
    
    @queryset_manager
    def myOwnUpdate(docs_cls,queryset):
        queryset.filter(internal__gte=128).update(inc__internal=128)
        # for x in queryset.filter(internal__gte=128):
        #     print(x)
    
    def initialize(self,a="",b=[],c="",d=0,e=0,f=0):
        self.brand=a
        self.features=b
        self.model=c
        self.price=d
        self.ram=e
        self.internal=f
    
    def __str__(self):
        return self.brand+" "+str(self.features)+" "+self.model+" "+str(self.price)+" "+str(self.ram)+" "+str(self.internal)

class Bike(Document):
    regno=StringField()
    model=StringField(max_length=255)
    brand=StringField(max_length=255)
    year=IntField(required=True)
    cc=FloatField()
    price=IntField()
    
    @queryset_manager
    def moreDeleteByRegno(docs_cls,queryset):
        docx=queryset.filter(regno="TN54U9478")
        for x in docx:
            x.delete()
    
    def _init__(self,a="",b="",c="",d=0,e=0.0,f=0):
        print("Constructor called")
        self.regno=a
        self.model=b
        self.brand=c
        self.year=d
        self.cc=e
        self.price=f
    
    def __str__(self):
        return "Bike informations are "+self.regno+" "+self.model+" "+self.brand+" "+str(self.year)+" "+str(self.cc)+" "+str(self.price)