from django.shortcuts import render
from . import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
# Create your views here.
def index(request):
    products =  models.Product.objects.all()
    return render(request,'index.html',{'products': products})
def buy(request):
    productName= request.GET.get('product','')
    product = models.Product.objects.get(name = productName)
    product.stock_balance-=1
    product.save()
    order =models.Order()
    order.buyer = User.objects.get(username = 'Вова')
    order.product = product
    order.orderNumber = order.getOrderNumber()
    order.save()
    return render(request,'success.html',{'param':productName , 'stock_balance': product.stock_balance, 'orderNumber': order.orderNumber})
def showOrders(request):
    buys=models.Order.objects.all()
    return render(request,'orders.html',{'buys': buys})
