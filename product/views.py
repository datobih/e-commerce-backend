from math import prod
from turtle import title
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import OrderItem, Product
from .serializers import OrderItemSerializer, ProductSerializer,AddOrderSerializer
from rest_framework.response import Response
# Create your views here.


class GetAllProducts(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        products=Product.objects.all()
        
        serializer=ProductSerializer(products,many=True)

        print(serializer.data)
        return Response(serializer.data)

class AddOrderItem(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data
        serializer=AddOrderSerializer(data=data)
        is_valid=serializer.is_valid()
        if(not is_valid):
            return serializer.errors
        product_title=data['product']
        quantity=data['quantity']
        try:
            order_item=OrderItem.objects.get(product__title=product_title,paid=False)
            order_item.quantity=order_item.quantity+quantity
            order_item.save()

        except OrderItem.DoesNotExist as e:
            product=Product.objects.get(title=product_title)
            order_item=OrderItem.objects.create(product=product,quantity=quantity,
            user=request.user)
            order_item.save()

            order_data=OrderItemSerializer(order_item).data

        return Response(status=200,data=order_data)




