from django.urls import path
from .views import (
    GetAllProducts,AddOrderItem,
    GetCartItems, MakePayment, ProductDetailView,RemoveOrderItemView,
    GetPurchasedItems

)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('all/',GetAllProducts().as_view(),name='all-products'),
   path('add-item/',AddOrderItem.as_view(),name='add-items'),
   path('get-cart/',GetCartItems.as_view(),name='get-cart'),
   path('make-payment/',MakePayment.as_view(),name='make-payment'),
   path('product-detail/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
   path('remove-order/',RemoveOrderItemView.as_view(),name='remove-order'),
   path('get-purchased-products/',GetPurchasedItems.as_view(),name='get-purchased-items')


]