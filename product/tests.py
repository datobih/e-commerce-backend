import email
from itertools import product
from unicodedata import category
from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Vendor
from product.models import OrderItem, Product
from rest_framework_simplejwt.tokens import RefreshToken

endpoint=reverse('all-products')
add_items_endpoint=reverse('add-items')
get_cart_endpoint=reverse('get-cart')
make_payment_endpoint=reverse('make-payment')
# Create your tests here.

class BaseTestCase(TestCase):
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
        
        self.init_products()
        self.init_order_items()

        self.auth_header=f'Bearer {self.access}'
        return super().setUp()   


class TestProducts(BaseTestCase):

    def init_products(self):
        self.product=Product(title="Iphone13",description="Brand new iPhone",
        price="700000",category="Phones",vendor=self.vendor)
        self.product_1=Product(title="HP Omen 13",description="Brand new HP Omen 13",
        price="700000",category="Laptops",vendor=self.vendor)
        self.product.save()
        self.product_1.save()
    

    def init_order_items(self):
        self.order_item=OrderItem.objects.create(product=self.product,quantity=2,user=self.user)
        self.order_item_1=OrderItem.objects.create(product=self.product_1,quantity=1,
        user=self.user)





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

    def test_get_cart(self):
        response=self.client.get(get_cart_endpoint,content_type='application/json',
        HTTP_AUTHORIZATION=self.auth_header)
        print(response.json())

    def test_make_payment(self):
        response=self.client.post(make_payment_endpoint,
        HTTP_AUTHORIZATION=self.auth_header,data={'item_id':[self.order_item.pk,self.order_item_1.pk]},
        content_type='application/json')
        print(response.json())
        print(OrderItem.objects.filter(paid=True))





