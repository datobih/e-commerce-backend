from django.urls import path
from .views import GetAllProducts
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('all/',GetAllProducts().as_view(),name='all-products') 
    


]