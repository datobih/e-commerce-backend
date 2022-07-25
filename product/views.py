from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer,AddOrderSerializer
from rest_framework.response import Response
# Create your views here.


class GetAllProducts(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products)
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
        product=data['product']
        quantity=data['quantity']



