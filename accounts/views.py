from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class CreateUserView(APIView):
    def post(self,request):
        data=request.data
        serializer= CreateUserSerializer(data=data)
        serializer.is_valid(True)
        user=serializer.save()

        return Response({'email':user.email})


class BlacklistRefreshToken(APIView):
    def post(self,request):
        data=request.data
        if('refresh' in data):
            refresh=data['refresh']
            token=RefreshToken(refresh)
            token.blacklist()
            return Response(status=200)
            
