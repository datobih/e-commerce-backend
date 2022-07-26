from math import prod
from tkinter.tix import Tree
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


class GetCartItems(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        order_items=OrderItem.objects.filter(user=request.user,paid=False)
        data=OrderItemSerializer(order_items,many=True).data
        return Response(data=data)

class MakePayment(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        if('item_id' in data):
            if(type(data['item_id']) is list):
                print("IS LIST")
                total_cost=0
                order_item_list=[]
                for item in data['item_id']:
                    order_item=OrderItem.objects.get(pk=item)
                    order_item_list.append(order_item)

                    total_cost=total_cost+(int(order_item.product.price)*order_item.quantity)

                print(order_item_list)
                balance=int(user.account_balance)

                if(total_cost<balance):
                    balance=balance-total_cost
                    user.account_balance=str(balance)
                    user.save()
                    for item in order_item_list:
                        item.paid=True
                        item.save()

                else:
                    return Response({'message':"Insufficient balance"})

                return Response({'message':"Transaction successful"})
                    



        return Response(status=400)


