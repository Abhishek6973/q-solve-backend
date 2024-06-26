from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #1
    path('register/student/',UserRegistrationView.as_view(), name = 'StudentRegister'), #2
    path('login/user/', UserLoginView.as_view(), name  = "UserLogin"),
    path('login/user/reset', ResetPassword.as_view(), name  = "reset"),
    path('getUserByToken/', GetUserByToken.as_view(), name  = "getUserByToken"),
    path('sendOtp/',ForgotPasswordView.as_view(), name  = "sendOtp"),
    path('passwordReset/', PasswordResetView.as_view(), name  = 'passwordReset'), 
]