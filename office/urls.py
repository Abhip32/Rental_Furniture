from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('oindex1', views.oindex1, name='oindex1'),
    path('oindex2', views.oindex2, name='oindex2'), 
    path('oindex3', views.oindex3, name='oindex3'), 
    path('oindex4', views.oindex4, name='oindex4'),
    path('oindex5', views.oindex5, name='oindex5'),    
    path('oindex6', views.oindex6, name='oindex6'),
    path('oindex7', views.oindex7, name='oindex7'), 
    path('oindex8', views.oindex8, name='oindex8'),    
    path('oindex9', views.oindex9, name='oindex9'),
    path('oindex10', views.oindex10, name='oindex10'),     
    path('oindex11', views.oindex11, name='oindex11'),     
    path('oindex12', views.oindex12, name='oindex12'), 
    path('oindex13', views.oindex13, name='oindex13'),
    path('oindex14', views.oindex14, name='oindex14'),
    path('oindex15', views.oindex15, name='oindex15'),
]