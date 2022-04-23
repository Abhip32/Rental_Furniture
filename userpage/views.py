from django.shortcuts import render
from flask import session
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from cart.models import Cart,Invoice
from cart.models import Order
from django.contrib.auth.models import User
import time
from django.contrib import messages
from createuser.models import Adduser

# Create your views here.
def index(request):
       odd=Order.objects.all()
       return render(request,"userpage.html",{'od':odd})

def update(request):
       if request.method == 'POST':
         if 'uid' in request.session:
               uid = request.session['uid']
         user=Adduser.objects.filter(username=uid)
         od=Order.objects.filter(username=uid)
         us=User.objects.filter(username=uid)
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
         for items in user:
                items.Password= request.POST.get('Password');
                items.Fname= request.POST.get('Fname');
                items.Lname= request.POST.get('Lname');
                items.Address= request.POST.get('Address');
                items.Phone_No= request.POST.get('Phone_No');
                items.Email= request.POST.get('Email');
                items.save()
         u = User.objects.get(username=uid)
         u.set_password(request.POST.get('Password'))
         u.save()
         
         

       return render(request,"userpage.html",{'u':uid,'od':od,'ad':Add,'g':greet,'inv':inv})


def track(request):
       if request.method == 'POST':
         if 'uid' in request.session:
               uid = request.session['uid']
         user=Adduser.objects.filter(username=uid)
         od=Order.objects.filter(username=uid)
         us=User.objects.filter(username=uid)
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
         tid=0
         tid=request.POST.get('ID')
         order=Order.objects.filter(id=tid)
         status=[""]
         for items in order:
              if(items.progress=="0"):
                     status=["Processing of Order will start soon"]
              if(items.progress=="20"):
                     status=["Order Placed and it is wating for pickup"]
              if(items.progress=="40"):
                     status=["Order Placed and it is wating for pickup","Order got picked up"]
              if(items.progress=="60"):
                     status=["Order Placed and it is wating for pickup","Order got picked up","Order is in transist"]
              if(items.progress=="80"):
                     status=["Order Placed and it is wating for pickup","Order got picked up","Order is in transist","Order reached at final destination"]
              if(items.progress=="100"):
                     status=["Order Placed and it is wating for pickup","Order got picked up","Order is in transist","Order reached at final destination","Order Delivered Successfully"]
              
       return render(request,"userpage.html",{'u':uid,'od':od,'ad':Add,'g':greet,'inv':inv,'pro':order,'sta':status})

def cancel(request):
       if request.method == 'POST':
         if 'uid' in request.session:
               uid = request.session['uid']
         user=Adduser.objects.filter(username=uid)
         od=Order.objects.filter(username=uid)
         us=User.objects.filter(username=uid)
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
         tid=0
         tid=request.POST.get('ID')
         order=Order.objects.filter(id=tid)
         status=[""]
         for items in order:
              if(items.progress<"100"):
                     messages.info(request, 'Your Order Got Cancelled .')
                     messages.info(request, 'Our agent will be in your touch soon')
                     items.delete()
              else:
                    messages.info(request, 'As order has already delivered, we cannot proceed further')
              
              
       return render(request,"userpage.html",{'u':uid,'od':od,'ad':Add,'g':greet,'inv':inv,'pro':order,'sta':status})