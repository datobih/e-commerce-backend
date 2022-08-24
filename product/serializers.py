from dataclasses import field
from email.mime import image
from itertools import product

from rest_framework import serializers
from .models import OrderItem, Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(source='pk')
    vendor=serializers.CharField(source='vendor.name')
    images=serializers.SerializerMethodField('get_product_images',required=False)
    class Meta:
        model=Product
        fields=['title','description','price','discount','category','vendor','images','id']


    def get_product_images(self,obj):
        image_list=[]
        print(obj)
        print(obj.images.all())
        for product_image in obj.images.all():
            image_list.append(product_image.image.url)
        return image_list





class AddOrderSerializer(serializers.Serializer):
    pk=serializers.IntegerField()
    quantity=serializers.IntegerField()


class OrderItemSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(source='pk')
    product=serializers.CharField(source='product.title')
    price=serializers.CharField(source='product.price')
    images=serializers.SerializerMethodField('get_product_images',required=False)
    class Meta:
        model=OrderItem
        fields=['quantity','product','price','images','id']



    def get_product_images(self,obj):
        image_list=[]
        print(obj)
        print(obj.product.images.all())
        for product_image in obj.product.images.all():
            image_list.append(product_image.image.url)
        return image_list

# class SimpleOrderItemSerializer(serializers.Serializer):
#     product=serializers.CharField()
#     quantity=serializers.IntegerField()


# class PurchaseOrderItemSerializer(serializers.Serializer):
#     order_items=serializers.ListSerializer(child=SimpleOrderItemSerializer())
