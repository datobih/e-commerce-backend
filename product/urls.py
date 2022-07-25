from django.urls import path
from .views import GetAllProducts,AddOrderItem
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('all/',GetAllProducts().as_view(),name='all-products'),
   path('add-item/',AddOrderItem.as_view(),name='add-items') 
    


]