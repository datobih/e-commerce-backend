from math import prod
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


class ProductDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        ratings=product.ratings.all()
        total_rating=0
        for rating in ratings:
            total_rating+=rating.stars
        if(ratings.count()==0):
            average_rating=0
        else:
            average_rating=total_rating/ratings.count()
        serializer=ProductSerializer(product)
        data=serializer.data
        data['average_rating']=average_rating
        data['rating_count']=ratings.count()
        return Response(data)



class AddOrderItem(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):
        data=request.data
        serializer=AddOrderSerializer(data=data)
        is_valid=serializer.is_valid()
        if(not is_valid):
            return Response(serializer.errors)
        product_pk=data['pk']
        quantity=data['quantity']
        print(data)
        try:
            order_item=OrderItem.objects.get(product__pk=product_pk,paid=False)
            order_item.quantity=(order_item.quantity+quantity)
            order_item.save()
            order_data=OrderItemSerializer(order_item).data

        except OrderItem.DoesNotExist as e:
            product=Product.objects.get(pk=product_pk)
            order_item=OrderItem.objects.create(product=product,quantity=quantity,
            user=request.user)
            order_item.save()

            order_data=OrderItemSerializer(order_item).data

        return Response(status=200,data=order_data)


class RemoveOrderItemView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        if(len(data)==1):
            if('pk' in data):
                try:
                    print(data['pk'])
                    order_item=OrderItem.objects.get(pk=int(data['pk']))
                    print(order_item)
                    order_item.delete()
                    return Response(status=200)
                except:
                    print("NOT FOUND")
                    return Response(status=400,data={'error':'pk not valid'})



        return Response(status=400,data={'error':'Wrong data provided'})


class GetCartItems(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        order_items=OrderItem.objects.filter(user=request.user,paid=False)
        data=OrderItemSerializer(order_items,many=True).data
        return Response(data=data)


class GetPurchasedItems(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        order_items=OrderItem.objects.filter(user=request.user,paid=True)
        data=OrderItemSerializer(order_items,many=True).data
        return Response(data=data)

class MakePayment(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        if('password' in data):
            if(not isinstance(data['password'],str)):
                return Response(status=400)
            if(not user.check_password(data['password'])):
                return Response({'message':'Invalid password'})


            order_items=OrderItem.objects.filter(paid=False,user=user)
            total_cost=0
            for order_item in order_items:
                total_cost+= int(order_item.product.price)

            balance=int(user.account_balance)

            if(total_cost<=balance):
                balance=balance-total_cost
                user.account_balance=str(balance)
                user.save()
                for item in order_items:
                    item.paid=True
                    item.save()

            else:
                return Response({'message':"Insufficient balance"})

            return Response({'message':"Transaction successful"})
                    



        return Response(status=400)


