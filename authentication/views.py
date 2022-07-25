from re import A
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ActivationToken
from rest_framework_simplejwt.tokens import RefreshToken
import traceback

# Create your views here.
class ActivateUserAccount(APIView):
    def post(self,request):
        print("ACTIVATE")
        data=request.data
        if ('otp' in data):
            try:
                activation_token=ActivationToken.objects.get(token=data['otp'])
                user=activation_token.user
                user.is_active=True
                user.save()
                activation_token.delete()
                refresh=RefreshToken.for_user(user=user)
                return Response({
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                })
            except Exception as e:
                
                traceback.print_exc()


        return Response(status=400)