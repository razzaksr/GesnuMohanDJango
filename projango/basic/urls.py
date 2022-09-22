from django.urls import path
from . import views

urlpatterns = [
    path('',views.myBegin),
    path('ins',views.myInsert),
    path('show',views.myShow),
    path('read/<str:number>',views.myRead),
    path('readex',views.myReadIgnoring),
    path('readfi',views.myReadRequiring),
    path('readon',views.myReadOnly),
    path('del',views.myDelete),
    path('dels',views.myDeletes),
    path('mobs',views.myMobileView),
    path('mobcost',views.myMobileQuerys),
    path('mobin',views.myMobileQuerysIn),
    path('mobord',views.myMobileArrange),
    path('mobup',views.myMobileCustomUp),
    path('mobcase',views.myMobileCustomUp2),
    path('mobmodel',views.myMobileCustomUp3)
]
