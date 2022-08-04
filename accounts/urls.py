from django.urls import path
from .views import CreateUserView,LoginUserView,GetUserDataView

app_name='accounts'

urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name='create-user'),
    path('login-user/',LoginUserView.as_view(),name='login-user'),
    path('user-data/',GetUserDataView.as_view(),name='user-data')
]