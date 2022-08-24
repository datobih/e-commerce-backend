from requests import request
from rest_framework import serializers
from django.contrib.auth import get_user_model

from authentication.models import ActivationToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import binascii
import os


User=get_user_model()

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()



    def validate(self, attrs):
        super().validate(attrs)
        request=self.context['request']

        user=authenticate(username=attrs['email'],password=attrs['password'])
        print(user.email)
        refresh_token=RefreshToken.for_user(user)
        attrs['refresh_token']=str(refresh_token)
        attrs['access_token']=str(refresh_token.access_token)



        return attrs 


class UserDataSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField('get_profile_picture',required=False)


    class Meta:
        model=User
        fields=['email','fullname','profile_picture','address',
        'account_balance','is_active']

    def get_profile_picture(self,obj):
        if(obj.profile_picture):
            return obj.profile_picture.url
        return ""

class CreateUserSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    password1=serializers.CharField()

    def validate(self, attrs):
        super().validate(attrs)

        if(attrs['password']==attrs['password1']):
            return attrs

        raise serializers.ValidationError("The passwords are not the same")




    def create(self, validated_data):
        email=validated_data['email']
        password=validated_data['password']
        fullname=validated_data['fullname']
        user=User.objects.create_user(email=email,
        password=password,fullname=fullname
        )
        activation_token=ActivationToken(user=user)
        activation_token.token=binascii.hexlify(os.urandom(3)).decode()
        activation_token.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=User
        fields=['fullname','email','address']

    def update(self, instance, validated_data):
        print(validated_data)
        return super().update(instance, validated_data)
    
