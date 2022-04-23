from django.shortcuts import render
from office.models import Stock
from cart.models import Cart
from cart.models import OutOfStock
# Create your views here.
def index(request):
    if 'uid' in request.session:
      uid = request.session['uid']
      obj=Stock.objects.all()
      for items in obj:
          if int(items.Product_Quantity)<=0:
              os=OutOfStock(id=items.Product_Name,Catagory="Office")
              os.save()
      return render(request,"office.html",{'u':uid})
    
    return render(request,"office.html")

def oindex1(request):
    if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Kids Study Solution",price=580,url="static/Images/off1.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Kids Study Solution":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Kids Study Solution",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o1':"Out of Stock"})
          
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
    return render(request,"office.html",{'u':uid})
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)

def oindex2(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vitello Pro Workstation",price=680,url="static/Images/off2.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vitello Pro Workstation":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vitello Pro Workstation",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o2':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})
   #new_pro = Cart(name="Bordo Queen Bedroom",price=600,url="static/Images/b3.jpg",total=0,User=uid)

def oindex3(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Lana Workstation",price=580,url="static/Images/off3.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Lana Workstation":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Lana Workstation",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o3':"Out of Stock"})
          
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex4(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Vitello Workstation",price=980,url="static/Images/off4.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Vitello Workstation":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Vitello Workstation",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o4':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex5(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="MIlli workstation-Pro",price=740,url="static/Images/off5.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="MIlli workstation-Pro":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="MIlli workstation-Pro",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o5':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex6(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Roo Study Table",price=820,url="static/Images/off6.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Roo Study Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Roo Study Table",Product_Price="820",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o6':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})

def oindex7(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Office Chair",price=980,url="static/Images/off7.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Office Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Office Chair",Product_Price="980",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o7':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex8(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Aero Chair",price=740,url="static/Images/off8.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Aero Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Aero Chair",Product_Price="740",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o8':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex9(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Flexo Chair",price=1180,url="static/Images/off9.webp.jpg",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Flexo Chair":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Flexo Chair",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o9':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex10(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Mini Workstation",price=1180,url="static/Images/off10.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Mini Workstation":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Mini Workstation",Product_Price="1180",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o10':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex11(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Roo Teak Table",price=900,url="static/Images/off11.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Roo Teak Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Roo Teak Table",Product_Price="900",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o11':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex12(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Nauka Center",price=1140,url="static/Images/off12.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Nauka Center":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Nauka Center",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o12':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex13(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Nauka Study Table",price=580,url="static/Images/off13.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Nauka Study Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Nauka Study Table",Product_Price="580",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o13':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex14(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Maria Table",price=680,url="static/Images/off14.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Maria Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Maria Table",Product_Price="680",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o14':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})


def oindex15(request):
  if request.method=="POST":
      uid=None
      if 'uid' in request.session:
          uid = request.session['uid']
          new_pro = Cart(name="Folding Utility Table",price=1140,url="static/Images/off15.webp",total=0,User=uid)
          St=Stock.objects.all()
          for items in St:
              if items.Product_Name=="Folding Utility Table":
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name="Folding Utility Table",Product_Price="1140",Product_Quantity=quan)
                  ps.save()
                  if(int(quan)>0):
                      new_pro.save()
                  else:
                     return render(request,"office.html",{'u':uid,'o15':"Out of Stock"})
          return render(request,"office.html",{'u':uid})
      else:
          return render(request,"login.html")
  return render(request,"office.html",{'u':uid})

