from asyncio.windows_events import NULL
from django.shortcuts import render
from cart.models import Cart
from bedroom.models import Stock
from cart.models import OutOfStock
from django.shortcuts import redirect
# Create your views here.
def index(request):
  if 'uid' in request.session:
      uid = request.session['uid']
      obj=Stock.objects.all()
      for items in obj:
          if int(items.Product_Quantity)<=0:
              os=OutOfStock(id=items.Product_Name,Catagory="Bedroom")
              os.save()

      return render(request,"bedroom.html",{'u':uid})
  return render(request,"bedroom.html")


def index1(request):
    if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Bedroom",price=580,url="static/Images/b1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Bedroom",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o1':"Out of Stock"})
          
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
    return render(request,"bedroom.html",{'u':uid})
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)

def index2(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Pico Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Pico Queen Bedroom",Product_Price="920",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o2':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})
   #new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)

def index3(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bordo Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bordo Queen Bedroom",Product_Price="600",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o3':"Out of Stock"})
          
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index4(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli Divi Queen Bedroom",price=980,url="static/Images/b4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli Divi Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli Divi Queen Bedroom",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o4':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index5(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Summer Blush Bedroom",price=740,url="static/Images/b5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Summer Blush Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Summer Blush Bedroom",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o5':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index6(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Queen Bedroom",price=820,url="static/Images/b6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Queen Bedroom",Product_Price="820",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o6':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})

def index7(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Amigo Queen Bedroom",price=980,url="static/Images/b10.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Amigo Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Amigo Queen Bedroom",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o7':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index8(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Santorini Queen Bedroom",price=740,url="static/Images/b11.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Santorini Queen Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Santorini Queen Bedroom",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o8':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index9(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bordo King Bedroom",price=1180,url="static/Images/b12.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bordo King Bedroom":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bordo King Bedroom",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o9':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index10(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Queen Bed",price=1180,url="static/Images/sb1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Queen Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Queen Bed",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o10':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index11(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Single Bed",price=900,url="static/Images/sb2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Single Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Single Bed",Product_Price="900",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o11':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index12(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Queen Single Bed",price=1140,url="static/Images/sb3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Queen Single Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Queen Single Bed",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o12':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index13(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vitello Single Bed",price=580,url="static/Images/s1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vitello Single Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vitello Single Bed",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o13':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index14(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Pico Single Bed",price=680,url="static/Images/s2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Pico Single Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Pico Single Bed",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o14':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index15(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vitello Twin Bed",price=1140,url="static/Images/s3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vitello Twin Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vitello Twin Bed",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o15':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index16(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli Dvi Queen Bed",price=360,url="static/Images/s4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli Dvi Queen Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli Dvi Queen Bed",Product_Price="360",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o16':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index17(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vitello Queen Bed",price=720,url="static/Images/s5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vitello Queen Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vitello Queen Bed",Product_Price="720",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o17':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index18(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Allen Queen Basic Bed",price=720,url="static/Images/s6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Allen Queen Basic Bed":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Allen Queen Basic Bed",Product_Price="720",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o18':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index19(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bounce",price=860,url="static/Images/m1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bounce":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bounce",Product_Price="860",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o19':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})


def index20(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bounce M",price=920,url="static/Images/m2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bounce M":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bounce M",Product_Price="920",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"bedroom.html",{'u':uid,'o20':"Out of Stock"})
          return render(request,"bedroom.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"bedroom.html",{'u':uid})
