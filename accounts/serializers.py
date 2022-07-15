from rest_framework import serializers
from django.contrib.auth import get_user_model


User=get_user_model()

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
        return user


    