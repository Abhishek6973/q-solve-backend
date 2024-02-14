from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from .models import User, Question
from .serializers import *

def gettokensforuser(student):
    refresh = RefreshToken.for_user(student)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    

# Generate token manully for admin
def gettokensforexpert(admin):
    refresh = RefreshToken.for_user(admin)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_active=False)
        token = gettokensforuser(user)
        return Response(
            {"token": token, "msg": "Registration Successful"},
            status=status.HTTP_201_CREATED,
        )
