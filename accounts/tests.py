from operator import truediv
from select import select
from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
import json
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
class BaseTestCase(APITestCase):
    def setUp(self) -> None:

        self.User=get_user_model()
        registeration_credentials={
            'email':'test@gmail.com',
            'fullname':'Test User',
            'password':'testuser123',
        }
        self.user=self.User.objects.create_user(**registeration_credentials)
        self.user.is_active=True
        self.user.save()
        self.token=RefreshToken.for_user(user=self.user)




class AccountTestCase(BaseTestCase):
    def test_user_setup(self):
        self.assertEquals('test@gmail.com',self.user.email)

    def test_create_endpoint(self):
        create_endpoint=reverse('accounts:create-user')
        credentials={'fullname':'User 2',
        'email':'user2@gmail.com',
        'password':'user21234',
        'password1':'user21234'}
        response=self.client.post(create_endpoint,data=credentials)
        response_data=response.json()
        print(response_data)
        self.assertEquals('user2@gmail.com',response_data['email'])


    def test_login_endpoint(self):
        login_endpoint=reverse('accounts:login-user')
        credentials={'email':'test@gmail.com',
        'password':'testuser123',
        'confirm_password':'testuser123'}
        response=self.client.post(login_endpoint,credentials)
        print(response.json())



    def test_get_user_data_endpoint(self):
        access_token=str(self.token.access_token)
        user_data_endpoint=reverse('accounts:user-data')
        auth_header=f'Bearer {access_token}'
        response=self.client.get(user_data_endpoint,HTTP_AUTHORIZATION=auth_header,
        content_type='application/json')
        print(response.json())


    
