from asyncio.windows_events import NULL
from django.shortcuts import render
from cart.models import Cart
from living_room.models import Stock
from cart.models import OutOfStock
from django.shortcuts import redirect
# Create your views here.
def index(request):
  if 'uid' in request.session:
      uid = request.session['uid']
      obj=Stock.objects.all()
      for items in obj:
          if int(items.Product_Quantity)<=0:
              os=OutOfStock(id=items.Product_Name,Catagory="Living Room")
              os.save()
      return render(request,"living_room.html",{'u':uid})
  return render(request,"living_room.html")
def lrindex1(request):
    if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flex L-Shaped Living Room",price=580,url="static/Images/sofa1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flex L-Shaped Living Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flex L-Shaped Living Room",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o1':"Out of Stock"})
          
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
    return render(request,"living_room.html",{'u':uid})
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)

def lrindex2(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flex L-Shaped Living Liliac",price=680,url="static/Images/sofasa2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flex L-Shaped Living Liliac":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flex L-Shaped Living Liliac",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o2':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})
   #new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)

def lrindex3(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli L-Shaped Living Room",price=580,url="static/Images/sofa3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli L-Shaped Living Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli L-Shaped Living Room",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o3':"Out of Stock"})
          
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex4(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Milli L-Shaped Living (Grey)",price=980,url="static/Images/sofa4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Milli L-Shaped Living (Grey)":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Milli L-Shaped Living (Grey)",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o4':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex5(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flex Two Sitter - Lilac",price=740,url="static/Images/sofa5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flex Two Sitter - Lilac":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flex Two Sitter - Lilac",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o5':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex6(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="OSO Three Seater",price=820,url="static/Images/sofa6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="OSO Three Seater":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="OSO Three Seater",Product_Price="820",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o6':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})

def lrindex7(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flex Five Sitter Set",price=980,url="static/Images/sofas1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flex Five Sitter Set":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flex Five Sitter Set",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o7':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex8(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Liliac Five Sitter Set",price=740,url="static/Images/sofas2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Liliac Five Sitter Set":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Liliac Five Sitter Set",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o8':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex9(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Azure Five Sitter Set",price=1180,url="static/Images/sofas4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Azure Five Sitter Set":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Azure Five Sitter Set",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o9':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex10(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Amor Living Room",price=1180,url="static/Images/sofas5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Amor Living Room":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Amor Living Room",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o10':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex11(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flex Five Sitter -Liliac",price=900,url="static/Images/sofas6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flex Five Sitter -Liliac":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flex Five Sitter -Liliac",Product_Price="900",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o11':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex12(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vive Five Sitter",price=1140,url="static/Images/sofas9.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vive Five Sitter":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vive Five Sitter",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o12':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex13(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="The Lounger",price=580,url="static/Images/re1.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="The Lounger":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="The Lounger",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o13':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex14(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Twin Adobe",price=680,url="static/Images/re2.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Twin Adobe":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Twin Adobe",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o14':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex15(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Fabric Lounger Teal",price=1140,url="static/Images/re3.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Fabric Lounger Teal":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Fabric Lounger Teal",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o15':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex16(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Fluent Motorised Recliner",price=360,url="static/Images/re4.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Fluent Motorised Recliner":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Fluent Motorised Recliner",Product_Price="360",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o16':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex17(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Blurt Motorised Recliner",price=720,url="static/Images/re5.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Blurt Motorised Recliner":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Blurt Motorised Recliner",Product_Price="720",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o17':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex18(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="The Fabric Lounger Brick",price=720,url="static/Images/re6.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="The Fabric Lounger Brick":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="The Fabric Lounger Brick",Product_Price="720",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o18':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex19(request):
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
                     return render(request,"living_room.html",{'u':uid,'o19':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})


def lrindex20(request):
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
                     return render(request,"living_room.html",{'u':uid,'o20':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})



def lrindex21(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Bounce B",price=720,url="static/Images/Bounce.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Bounce M":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Bounce B",Product_Price="720",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"living_room.html",{'u':uid,'o20':"Out of Stock"})
          return render(request,"living_room.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"living_room.html",{'u':uid})