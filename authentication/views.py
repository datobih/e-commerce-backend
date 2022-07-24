from re import A
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ActivationToken
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class ActivateUserAccount(APIView):
    def post(self,request):
        data=request.data
        if ('otp' in data):
            try:
                activation_token=ActivationToken.objects.get(data['otp'])
                user=activation_token.user
                user.is_active=True
                activation_token.delete()
                refresh=RefreshToken.for_user(user=user)
                return{
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
            except:
                pass


        return Response(status=400)