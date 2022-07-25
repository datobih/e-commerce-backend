import email
from unicodedata import category
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Vendor
from product.models import Product
from rest_framework_simplejwt.tokens import RefreshToken

endpoint=reverse('all-products')
add_items_endpoint=reverse('add-items')
# Create your tests here.
class TestProducts(TestCase):
    def setUp(self) -> None:
        
        self.User=get_user_model()
        registeration_credentials={
            'email':'test@gmail.com',
            'fullname':'Test User',
            'password':'testuser123',
            'is_active':True
        }


        self.user=self.User.objects.create_user(**registeration_credentials)
        refresh=RefreshToken.for_user(user=self.user)
        self.access=refresh.access_token
        self.vendor=Vendor(user=self.user,name="Test Vendor",description="This is a test project")
        self.vendor.save()
        self.product=Product(title="Iphone13",description="Brand new iPhone",
        price="#700000",category="Phones",vendor=self.vendor)
        self.product.save()
        
        return super().setUp()



    def test_is_user_available(self):
        user=self.User.objects.get(email='test@gmail.com')
        print(user)
        self.assertEquals(user.email,'test@gmail.com')

    def test_get_all_products(self):
        auth_header=f'Bearer {self.access}'
        response=self.client.get(endpoint,HTTP_AUTHORIZATION=auth_header)
        print(response.json())

    def test_add_order_items(self):
        auth_header=f'Bearer {self.access}'
        response=self.client.post(add_items_endpoint,HTTP_AUTHORIZATION=auth_header,
        data={'product':'Iphone13','quantity':1},content_type='application/json')
        print(response.json())




