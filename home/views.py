
from django.shortcuts import render
from flask import session
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from cart.models import Cart,Invoice,Expired
from cart.models import Order
from cart.models import OutOfStock
from datetime import date, timedelta
import datetime
import time
from createuser.models import Adduser

# Create your views here.
def index(request):
    uid=None
    if 'uid' in request.session:
      uid = request.session['uid']
    od=Order.objects.all()
    today = date.today()
    for items in od:
        if str(today)>items.dateofreturn:
            ex=Expired(id=items.id,user=items.username,productname=items.productname,address=items.placeofreceiver)
            ex.save()


    return render(request,'index.html',{'u':uid})

def logout(request):
    Session.objects.all().delete()
    Cart.objects.all().delete()
    return render(request,'index.html')
    
def login(request):
    if 'uid' in request.session:
      uid = request.session['uid']
      od=Order.objects.filter(username=uid)
      Add=Adduser.objects.filter(username=uid)
      inv=Invoice.objects.filter(id=uid)
      current_hour = time.strptime(time.ctime(time.time())).tm_hour
      if current_hour < 12 :
          greet="Good Morning"
      elif current_hour == 12 :
          greet="Good Noon"
      elif current_hour > 12 and current_hour < 18 :
          greet="Good Aftrenoon"
      elif current_hour >= 18 :
          greet="Good Evening"
      return render(request,"userpage.html",{'u':uid,'od':od,'ad':Add,'g':greet,'inv':inv}) 
    else:
      return render(request,"login.html")





    
    

