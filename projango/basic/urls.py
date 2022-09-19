from django.urls import path
from . import views

urlpatterns = [
    path('',views.myBegin),
    path('ins',views.myInsert)
]
