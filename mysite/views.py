
from django.shortcuts import render
from django.contrib.auth.models import User 
# Create your views here
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from datetime import datetime
import time
from .models import Product_Category,Product
from .forms import OrderForm
from twilio.rest import TwilioRestClient

def sendsms(message):
    account_sid = "AC2cc122cef4e48252b937f91e23eeac64"
    auth_token = "2d6c6b390aec62f2c8c17e49fc9037eb"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+2348136823630", from_="+16164389791",
                                     body=message)

def index(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid:
            form.save()
            message=request.POST['Name']+request.POST['PhoneNo']
            sendsms(message)
    products_category=Product_Category.objects.order_by('id')
#     print time
    return render(request,'mysite/home.html',{'products':products_category,'form':form})

def Product_table(request):
	products_category=Product_Category.objects.order_by('id')
	return render(request,'mysite/product.html',{'products':products_category})

def details(request,product_id):
	products_requested=get_object_or_404(Product_Category,pk=product_id)
	products_detail=Product.objects.filter(Product_Category=products_requested)
	return render(request,'mysite/product_Detail.html',{'products_detail':products_detail})
    
