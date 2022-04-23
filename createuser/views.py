from django.shortcuts import render
from .models import Adduser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
                    
    try:
         if request.method == 'POST':
                post=Adduser()
                post.username= request.POST.get('username')
                post.Password= request.POST.get('Password')
                post.Fname= request.POST.get('Fname')
                post.Lname= request.POST.get('Lname')
                post.Address= request.POST.get('Address')
                post.Phone_No= request.POST.get('Phone_No')
                post.Email= request.POST.get('Email')
                post.Image=request.POST.get('upload')
                if len(post.Password)>=8:
                    if (len(post.username)!=0):
                         if (len(post.Fname)!=0):
                             if (len(post.Lname)!=0):
                                 if (len(post.Address)!=0):
                                     if (len(post.Phone_No)!=0):
                                         if (len(post.Email)!=0): 
                                             newpost= Adduser(username=post.username,Password=post.Password,Fname=post.Fname,Lname=post.Lname,Address=post.Address,Phone_No=post.Phone_No,Email=post.Email,Image=post.Image)
                                             user = User.objects.create_user(post.username,post.Email, post.Password)
                                             user.save()
                                             newpost.save()
                                             return render(request, 'login.html')
                                         else:  
                                            messages.info(request, 'Please fill all required fields')
                                     else:  
                                        messages.info(request, 'Please fill all required fields')
                                 else:  
                                    messages.info(request, 'Please fill all required fields')
                             else:  
                                messages.info(request, 'Please fill all required fields')
                         else:  
                             messages.info(request, 'Please fill all required fields')
                    else:  
                        messages.info(request, 'Please fill all required fields')
                else:  
                    messages.info(request, 'Please fill all required fields')
                    
                if(len(post.Password)<8):
                    messages.info(request, 'Total number of characters in password should be grearer than or equal to 8')
                    return render(request,"createuser.html")
                
    
    except:
        messages.info(request, 'Please try a diffrent username')

   

    return render(request,"createuser.html")

        
