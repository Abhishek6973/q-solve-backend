from django.urls import path
from .views import UserRegistrationView, UserLoginView





from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #1
    path('register/student/',UserRegistrationView.as_view(), name = 'StudentRegister'), #2
    path('login/user/', UserLoginView.as_view(), name  = "UserLogin")
    
]