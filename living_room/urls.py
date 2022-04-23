from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('lrindex1', views.lrindex1, name='lrindex1'),
    path('lrindex2', views.lrindex2, name='lrindex2'), 
    path('lrindex3', views.lrindex3, name='lrindex3'), 
    path('lrindex4', views.lrindex4, name='lrindex4'),
    path('lrindex5', views.lrindex5, name='lrindex5'),    
    path('lrindex6', views.lrindex6, name='lrindex6'),
    path('lrindex7', views.lrindex7, name='lrindex7'), 
    path('lrindex8', views.lrindex8, name='lrindex8'),    
    path('lrindex9', views.lrindex9, name='lrindex9'),
    path('lrindex10', views.lrindex10, name='lrindex10'),     
    path('lrindex11', views.lrindex11, name='lrindex11'),     
    path('lrindex12', views.lrindex12, name='lrindex12'), 
    path('lrindex13', views.lrindex13, name='lrindex13'),
    path('lrindex14', views.lrindex14, name='lrindex14'),
    path('lrindex15', views.lrindex15, name='lrindex15'),
    path('lrindex16', views.lrindex16, name='lrindex16'),
    path('lrindex17', views.lrindex17, name='lrindex17'),
    path('lrindex18', views.lrindex18, name='lrindex18'),
    path('lrindex19', views.lrindex19, name='lrindex19'),
    path('lrindex20', views.lrindex20, name='lrindex20'),
   path('lrindex21', views.lrindex21, name='lrindex21'),
]