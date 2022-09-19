from mongoengine import *

class Bike(Document):
    regno=StringField()
    model=StringField(max_length=255)
    brand=StringField(max_length=255)
    year=IntField(required=True)
    cc=FloatField()
    price=IntField()
    
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