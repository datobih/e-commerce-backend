from dataclasses import field
from itertools import product
from math import prod
from rest_framework import serializers
from .models import OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    vendor=serializers.CharField(source='vendor.name')
    class Meta:
        model=Product
        fields=['title','description','price','discount','category','vendor']

class AddOrderSerializer(serializers.Serializer):
    product=serializers.CharField()
    quantity=serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):
    product=serializers.CharField(source='product.title')
    
    class Meta:
        model=OrderItem
        fields='__all__'
