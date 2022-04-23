from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('cindex1',views.cindex1,name='cindex1'),
]