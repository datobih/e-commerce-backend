from ctypes import addressof
from email.policy import default
import imp
from itertools import product
from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import BooleanField
from django.utils.translation import gettext_lazy as _

from accounts.models import Vendor

# Create your models here.

User=get_user_model()





class Product(models.Model):
    tags=[('Phones','Phones'),
    ('Laptops','Laptops'),
    ('Electronics','Electronics'),
    ('Fashion','Fashion'),]
    title=models.CharField(max_length=50)
    description=models.TextField()
    #FOREIGN RELATED: ProductImage
    price=models.CharField(max_length=300)
    discount=models.IntegerField(default=0)
    category=models.CharField(max_length=50,choices=tags,default="Generic Product")
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


# class Order(models.Model):
#     create_date=models.DateTimeField(auto_now_add=True)
#     order_date=models.DateTimeField()
#     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
#     total_price=models.CharField(max_length=300)
#     paid=models.BooleanField(default=False)
#     address=models.CharField(max_length=300)




class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    paid=models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.Case,related_name='order_items')
    
    def __str__(self) -> str:
        return self.product.title




class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='ratings') #Each products should have a rating system
    stars=models.IntegerField()
    comment=models.CharField(max_length=300)

    def __str__(self) -> str:
        return str(self.stars)


class ProductImage(models.Model):
    image=models.ImageField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE,
    related_name='images')
