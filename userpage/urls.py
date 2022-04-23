from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('userpage',views.index,name="userpage"),
    path('update',views.update,name="update"),
    path('track',views.track,name="track"),
    path('cancel',views.cancel,name="cancel"),
]