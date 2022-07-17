import imp
from itertools import product
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()



class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Product(models.Model):
    carts=models.ManyToManyField(Cart)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField()
    price=models.CharField(max_length=300)
    discount=models.IntegerField(default=0)
    category=models

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE) #Each products should have a rating system
    stars=models.IntegerField()
    comment=models.CharField(max_length=300)






