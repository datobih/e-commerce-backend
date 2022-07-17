from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

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
        pass
