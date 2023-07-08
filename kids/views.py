from asyncio.windows_events import NULL
from django.shortcuts import render
from cart.models import Cart
from kids.models import Stock
from cart.models import OutOfStock
from django.shortcuts import redirect
# Create your views here.
def index(request):
  obj=Stock.objects.all()
  if 'uid' in request.session:
      uid = request.session['uid']
      cart=Cart.objects.filter(User=uid)
      total_sum = 0;
      for item in cart:
        total_sum=total_sum+int(item.price)
      uid = request.session['uid']
      return render(request,"kids.html",{'u':uid,'items':obj,'cart':cart,'total_sum':total_sum})
  return render(request,"kids.html",{'items':obj})




def kaddToCart(request):
    if request.method=="POST":
        quantity=request.POST.get('quantity')
        name=request.POST.get('name')
        price=request.POST.get('price')
        img=request.POST.get('img')
        St=Stock.objects.all()
        uid=None;
        if 'uid' in request.session:
          uid = request.session['uid']
          cart=Cart.objects.filter(User=uid)
          total_sum = 0;
          for item in cart:
            total_sum=total_sum+int(item.price)
          print(uid)
          new_pro = Cart(name=name,price=price,url=img,User=uid,quantity=quantity)
          for items in St:
              if items.Product_Name==name:
                  quan=str(int(items.Product_Quantity)-1)
                  ps=Stock(Product_Name=name,Product_Price=price,Product_Quantity=quan)
                  ps.save()
                  new_pro.save()     
          return render(request,"kids.html",{'u':uid,'alert':"Order Added",'items':St,'cart':cart,'total':total_sum})
        else:
            print("asd")
            return render(request,"kids.html",{'u':uid,'alert':"Login First",'items':St})
       
 
   # new_pro = Cart(name="Pico Queen Bedroom",price=920,url="static/Images/b2.jpg",total=0,User=uid)


