from re import sub
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.models import ActivationToken
from .serializers import CreateUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .serializers import LoginSerializer,UserDataSerializer,UpdateUserSerializer
from django.contrib.auth import authenticate

# Create your views here.


class CreateUserView(APIView):
    def post(self,request):
        data=request.data
        serializer= CreateUserSerializer(data=data)
        serializer.is_valid(True)
        user=serializer.save()
        activation_token=ActivationToken.objects.get(user=user)
        email_verify_token=activation_token.token
        #Convert template to string
        email_template_html=loader.render_to_string('authentication/email_activate.html',context={'otp':email_verify_token})
        subject="Activate Account"
        recipient_list=[user.email]
        email_from=settings.EMAIL_HOST_USER
        text_content=f"Activate this account with this OTP {email_verify_token}"
        #Send OTP to user email address
        email_message=EmailMultiAlternatives(subject=subject,body=email_verify_token,
        from_email=email_from,to=recipient_list
        )
        email_message.attach_alternative(email_template_html,'text/html')
        email_message.send()

        return Response(status=200)


class LoginUserView(APIView):
     def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data,context={'request':request})
        is_valid=serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors,status=400)
        refresh_token=serializer.validated_data['refresh_token']
        access_token=serializer.validated_data['access_token']
        response_data={'refresh':refresh_token,'access':access_token}
        return Response(response_data)


class GetUserDataView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        serializer=UserDataSerializer(user)
        return Response(serializer.data)


class TopUpBalanceView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        user=request.user
        if('amount' in data):
            if(isinstance(data['amount'],int)):
                user.account_balance=str(int(user.account_balance)+data['amount'])
                user.save()
                return Response(status=200)

        return Response(status=400)

        
class UpdateUserDetailsView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        print(data)
        user=request.user
        serializer=UpdateUserSerializer(user,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(status=200)
        else:
            return Response(status=400,data=serializer.errors)




class BlacklistRefreshToken(APIView):
    def post(self,request):
        data=request.data
        if('refresh' in data):
            refresh=data['refresh']
            token=RefreshToken(refresh)
            token.blacklist()
            return Response(status=200)
            
