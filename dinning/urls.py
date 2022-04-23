from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('dindex1', views.dindex1, name='dindex1'),
    path('dindex2', views.dindex2, name='dindex2'), 
    path('dindex3', views.dindex3, name='dindex3'), 
    path('dindex4', views.dindex4, name='dindex4'),
    path('dindex5', views.dindex5, name='dindex5'),    
    path('dindex6', views.dindex6, name='dindex6'),
    path('dindex7', views.dindex7, name='dindex7'), 
    path('dindex8', views.dindex8, name='dindex8'),    
    path('dindex9', views.dindex9, name='dindex9'),
]