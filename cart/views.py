from django.shortcuts import render
from numpy import product, save
from cart.models import Cart
from cart.models import Order
from django.db.models import Sum
from datetime import date, timedelta
from cart.models import Invoice
import datetime

from decimal import Decimal
import string    
from fpdf import FPDF
from createuser.models import Adduser
import random # define the random module  




# Create your views here.
def index(request):
    if 'uid' in request.session:
      uid = request.session['uid']
    products = Cart.objects.all()
    return render(request,"cart.html",{'list':products,'u':uid})

def cindex1(request):
    if 'uid' in request.session:
      uid = request.session['uid']
    products = Cart.objects.all()
    use=Adduser.objects.filter(username=uid)
    for items in use:
      ad=items.Address
    S = 10  # number of characters in the string.  
   # call random.choices() string module to find the string in Uppercase + numeric data.  
    for item in products.iterator():
             ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
             today = date.today()
             NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=3)
             ret=datetime.datetime.today()  + datetime.timedelta(days=33)
             neworder=Order(id=ran,img=item.url,username=uid,productname=item.name,dateoforder=today,dateofdelivery=NextDay_Date,price=item.price,status="Pending",dateofreturn=ret,progress="0",placeofsender="Mumbai",placeofreceiver=ad)
             neworder.save()
             
             

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Funrento",ln = 1, align = 'C')
    pdf.cell(200, 10, txt = "Invoice /Order Summery/ Bill",ln = 2, align = 'C')
    pdf.cell(200, 10, txt = "Invoice",ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "---------------------------------------------------------------------------",ln = 2, align = 'L')
    price=0
    for item in products.iterator():
       pdf.cell(200, 10, txt = "Product Name :"+str(item.name),ln = 2, align = 'L')
       pdf.cell(200, 10, txt = "Price :"+str(item.price),ln = 2, align = 'L')
       pdf.cell(200, 10, txt = "Date of Order:"+str(today),ln = 2, align = 'L')
       pdf.cell(200, 10, txt = "Date of Delivery:"+str(NextDay_Date),ln = 2, align = 'L')
       pdf.cell(200, 10, txt = "Date of Return:"+ str(ret),ln = 2, align = 'L')
       pdf.cell(200, 10, txt = "---------------------------------------------------------------------------",ln = 2, align = 'L')
    now = datetime.datetime.now()
    current_time = now.strftime("_%H_%M_%S")
    path="static/invoice/"+uid+str(today)+str(current_time)+".pdf"
    inv=Invoice(uid,path)
    inv.save()
    pdf.output(path)
    Cart.objects.all().delete()
    return render(request,"payment.html")
    





    


