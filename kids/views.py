from django.shortcuts import render
from django.shortcuts import render
from cart.models import Cart
from kids.models import Stock
from cart.models import OutOfStock
# Create your views here.
def index(request):
    if 'uid' in request.session:
      uid = request.session['uid']
      obj=Stock.objects.all()
      for items in obj:
          if int(items.Product_Quantity)<=0:
              os=OutOfStock(id=items.Product_Name,Catagory="Kids")
              os.save()
      return render(request,"kids.html",{'u':uid})
    return render(request,"kids.html")


# Create your views here.
def index(request):
    if 'uid' in request.session:
      uid = request.session['uid']
      return render(request,"kids.html",{'u':uid})
    return render(request,"kids.html")



def kindex1(request):
    if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bao the Crib",price=900,url="static/Images/kid1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bao the Crib":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bao the Crib",Product_Price="900",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o1':"Out of Stock"})
          
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
    return render(request,"kids.html",{'u':uid})
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)

def kindex2(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Kids Storage Bunk Bed",price=680,url="static/Images/kid2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Kids Storage Bunk Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Kids Storage Bunk Bed",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o2':"Out of Stock"})
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"kids.html",{'u':uid})
   #new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)

def kindex3(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Kids Study Bunk Bed",price=580,url="static/Images/kid3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Kids Study Bunk Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Kids Study Bunk Bed",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o3':"Out of Stock"})
          
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"kids.html",{'u':uid})


def kindex4(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Kids Open Storage",price=980,url="static/Images/kid4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Kids Open Storage":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Kids Open Storage",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o4':"Out of Stock"})
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"kids.html",{'u':uid})


def kindex5(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Tidy Tween Kids Storage",price=740,url="static/Images/kid5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Tidy Tween Kids Storage":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Tidy Tween Kids Storage",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o5':"Out of Stock"})
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"kids.html",{'u':uid})


def kindex6(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Shell n Drobe",price=820,url="static/Images/kid6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Shell n Drobe":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Shell n Drobe",Product_Price="820",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"kids.html",{'u':uid,'o6':"Out of Stock"})
          return render(request,"kids.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"kids.html",{'u':uid})





