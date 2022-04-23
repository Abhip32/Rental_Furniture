from plistlib import UID
from django.shortcuts import render
from django.contrib import messages
from createuser.models import Adduser
from resetpassword.models import OTPSTORAGE
import os
from django.contrib.auth.models import User
import math
import random
import smtplib

# Create your views here.
def index(request):
    uid = None
    if 'uid' in request.session:
      uid = request.session['uid']  
    return render(request,"resetpassword.html")

def reset(request):
  try:
    if request.method == 'POST':
                 username= request.POST.get('username')
                 user=Adduser.objects.filter(username=username)
                 for items in user:
                   email=items.Email
                 OTP=""
                 digits="0123456789"
                 for i in range(6):
                    OTP+=digits[math.floor(random.random()*10)]
                 
                 otp = OTP + " is your OTP"
                 newotp=OTPSTORAGE(password=OTP,user=username)
                 newotp.save()
                 msg= """From: FunRento
                         To: User\n
                         Subject: <OTP to reset password>\n
                         Hello User, Your OTP is \n"""+otp
                        
                 s = smtplib.SMTP('smtp.gmail.com', 587)
                 s.starttls()
                 s.login("samcrick32@gmail.com", "810523705")
                 emailid = email
                 s.sendmail('&&&&&&&&&&&',emailid,msg)
                 messages.info(request, 'OTP has been sent to your mail please check')

  except:
    messages.info(request, 'Something Went Wrong')
                  
  return render(request,"resetpassword.html")

def verify(request):
  try:
    if request.method == 'POST':
                 username= request.POST.get('username')
                 user=Adduser.objects.filter(username=username)
                 r=OTPSTORAGE.objects.all()
                 for items in r:
                   o=items.password
                   i=items.user
                 a = request.POST.get('otp')
                 if a == o:
                     user= request.POST.get('username')
                     password= request.POST.get('password')
                     u = User.objects.get(username=user)
                     u.set_password(password)
                     u.save()
                     OTPSTORAGE.objects.all().delete()
                     return render(request,"index.html")
                 else:
                    OTPSTORAGE.objects.all().delete()
                    messages.info(request, 'Wrong OTP')
                    return render(request,"resetpassword.html")
  except:
    messages.info(request, 'Something Went Wrong')

    OTPSTORAGE.objects.all().delete()
    return render(request,"resetpassword.html")


  


