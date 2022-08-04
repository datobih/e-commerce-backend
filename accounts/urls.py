from django.urls import path
from .views import CreateUserView,LoginUserView

app_name='accounts'

urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name='create-user'),
    path('login-user/',LoginUserView.as_view(),name='login-user')
]