from django.shortcuts import render
from cart.models import Cart
from dinning.models import Stock
from cart.models import OutOfStock

# Create your views here.
def index(request):
    if 'uid' in request.session:
      uid = request.session['uid']
      obj=Stock.objects.all()
      for items in obj:
          if int(items.Product_Quantity)<=0:
              os=OutOfStock(id=items.Product_Name,Catagory="Dinning")
              os.save()
      return render(request,"dining.html",{'u':uid})

    return render(request,"dining.html")



def dindex1(request):
    if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli Dinning Table",price=580,url="static/Images/dt1.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli Dinning Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli Dinning Table",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o1':"Out of Stock"})
          
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
    return render(request,"dining.html",{'u':uid})
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)

def dindex2(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Simple Dining Table",price=680,url="static/Images/dt2.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Simple Dining Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Simple Dining Table",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o2':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})
   #new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)

def dindex3(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli Comfort Chair",price=580,url="static/Images/dt3.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli Comfort Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli Comfort Chair",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o3':"Out of Stock"})
          
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


def dindex4(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Clare Dining Chair",price=980,url="static/Images/dt4.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Clare Dining Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Clare Dining Chair",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o4':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


def dindex5(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli Dining Room",price=740,url="static/Images/dt5.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli Dining Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli Dining Room",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o5':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


def dindex6(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vettelo Comfort Chair",price=820,url="static/Images/dt6.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vettelo Comfort Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vettelo Comfort Chair",Product_Price="820",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o6':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})

def dindex7(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Dualo 4 Sitter Dining Table",price=980,url="static/Images/dt7.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Dualo 4 Sitter Dining Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Dualo 4 Sitter Dining Table",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o7':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


def dindex8(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Pico Dining Room",price=740,url="static/Images/dt8.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Pico Dining Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Pico Dining Room",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o8':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


def dindex9(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bordo Dining Room",price=1180,url="static/Images/dt9.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bordo Dining Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bordo Dining Room",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"dining.html",{'u':uid,'o9':"Out of Stock"})
          return render(request,"dining.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"dining.html",{'u':uid})


