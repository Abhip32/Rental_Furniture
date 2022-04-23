from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from flask import request
from django.contrib import messages
from .models import Adduser


def index(request):
    if request.method == 'POST':
                 username= request.POST.get('username')
                 Password= request.POST.get('Password')
                 request.session['uid'] = username
                 if 'uid' in request.session:
                    uid = request.session['uid']
                 user = authenticate(username=username, password=Password)
                 if user is not None:
                        return render(request,"index.html",{'u':uid})
                 else:
                      messages.info(request, 'Invalid Login Credentials')
    return render(request,"login.html")




    
                

   