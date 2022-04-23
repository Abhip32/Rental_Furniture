from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name=''),
    path('logout',views.logout,name="logout"),
    path('log',views.login,name="log"),
]