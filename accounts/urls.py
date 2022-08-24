from django.urls import path
from .views import(
     CreateUserView,LoginUserView,GetUserDataView,
     TopUpBalanceView,UpdateUserDetailsView
)

app_name='accounts'

urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name='create-user'),
    path('login-user/',LoginUserView.as_view(),name='login-user'),
    path('user-data/',GetUserDataView.as_view(),name='user-data'),
    path('update-profile/',UpdateUserDetailsView.as_view(),name='update-profile'),
    path('topup-balance/',TopUpBalanceView.as_view(),name='topup-balance')
]