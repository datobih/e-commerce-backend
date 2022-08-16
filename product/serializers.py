from dataclasses import field
from email.mime import image
from itertools import product
from math import prod
from rest_framework import serializers
from .models import OrderItem, Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    vendor=serializers.CharField(source='vendor.name')
    images=serializers.SerializerMethodField('get_product_images',required=False)
    class Meta:
        model=Product
        fields=['title','description','price','discount','category','vendor','images']


    def get_product_images(self,obj):
        image_list=[]
        print(obj)
        print(obj.images.all())
        for product_image in obj.images.all():
            image_list.append(product_image.image.url)
        return image_list


class AddOrderSerializer(serializers.Serializer):
    product=serializers.CharField()
    quantity=serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):
    product=serializers.CharField(source='product.title')
    
    class Meta:
        model=OrderItem
        fields='__all__'

# class SimpleOrderItemSerializer(serializers.Serializer):
#     product=serializers.CharField()
#     quantity=serializers.IntegerField()


# class PurchaseOrderItemSerializer(serializers.Serializer):
#     order_items=serializers.ListSerializer(child=SimpleOrderItemSerializer())
