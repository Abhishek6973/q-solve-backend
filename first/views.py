from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .renderers import UserRenderer
import random
from rest_framework.permissions import IsAuthenticated
from .serializers import *
import first.config as config
from rest_framework_simplejwt.authentication import JWTAuthentication

def gettokensforuser(student):
    refresh = RefreshToken.for_user(student)
    print(student, type(student))
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
    def post(self, request, format=None):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save(is_active=False)

            return Response(
                {"message": "Registration Successful"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as err:
            print(err)
            return Response({
                'message': err.args
            },status=500)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                json_user = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'role': user.role,
                    'experience': user.experience_level
                }
                if user.check_password(serializer.validated_data['password']):
                    print(type(user))
                    token = gettokensforuser(user)
                    return Response({'token': token,'user': json_user,"message": "Login successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ResetPassword(APIView):

    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user = User.objects.get(email=email)

        user.set_password(password)
        user.save()

        return Response({'message':'changed'},status=200)


class GetUserByToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user)  
            return Response({'user': serializer.data})
        except Exception as err:
            return Response({'message': "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ForgotPasswordView(APIView):
    def post(self, request):
        try:
            email = request.data.get("email")
            print("email: ", email)
            if email:
                try:
                    user = User.objects.get(email=email)
                    if user:
                        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
                        print(otp)
                        user.reset_password_token = otp
                        user.save()
                        config.send_email(otp,email)
                        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
