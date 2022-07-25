from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
import json

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