"""Rental_Furniture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pathlib import Path
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('bedroom',include('bedroom.urls')),
    path('living_room',include('living_room.urls')),
    path('office',include('office.urls')),
    path('dining',include('dinning.urls')),
    path('kids',include('kids.urls')),
    path('cart',include('cart.urls')),   
    path('newuser',include('createuser.urls')),
    path('success',include('success.urls')),      
    path('login',include('login.urls')),
    path('userpage',include('userpage.urls')),  
    path('resetpassword',include('resetpassword.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
