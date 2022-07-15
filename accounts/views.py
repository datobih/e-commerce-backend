from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import CreateUserSerializer
from rest_framework.authtoken.models import Token
# Create your views here.


class CreateUserView(APIView):

    def post(self,request):
        data=request.data
        serializer= CreateUserSerializer(data=data)
        serializer.is_valid(True)
        user=serializer.save()
