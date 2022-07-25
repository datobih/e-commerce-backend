from django.urls import path
from .views import ActivateUserAccount

urlpatterns = [
    path('verify-email/',ActivateUserAccount.as_view(),name='activate-user')
]