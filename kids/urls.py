from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('kindex1', views.kindex1, name='kindex1'),
    path('kindex2', views.kindex2, name='kindex2'), 
    path('kindex3', views.kindex3, name='kindex3'), 
    path('kindex4', views.kindex4, name='kindex4'),
    path('kindex5', views.kindex5, name='kindex5'),    
    path('kindex6', views.kindex6, name='kindex6'),
]