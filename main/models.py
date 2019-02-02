from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    price =  models.IntegerField()
    stock_balance = models.IntegerField()
    def __str__(self):
        return self.name
class Order(models.Model):
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    orderNumber = models.IntegerField(default= 0)
    date = models.DateTimeField(default=timezone.now)
    stock_balance = models.IntegerField(default=0)
    def __str__(self):
        return self.buyer.username
    def getOrderNumber(self):
        num =Order.objects.order_by()
        if len(num)>0:
            return num[len(num)-1].orderNumber+1
        else:
            return 1
