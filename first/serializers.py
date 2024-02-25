from rest_framework import serializers
from .models import User

msg = "Token is not Valid or Expired"

class UserRegistrationSerializer(serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ["email", "name", "password", "experience_level", "role"]
        extra_kwargs = {"password": {"write_only": True}}
        
    # def validate(self, attrs):
    #     password = attrs.get("password")
    #     password2 = attrs.get("password2")
    #     if password != password2:
    #         raise serializers.ValidationError(
    #             "Password and Confirm Password don't match" )
        
    #     return attrs
    def create(self, validated_data):
        # validated_data.pop("password2", None)
        user = User(**validated_data)
        user.set_password(validated_data["password"])  # Hash the password
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError('User does not exist')

            if not user.check_password(password):
                raise serializers.ValidationError('Invalid credentials password')
        else:
            raise serializers.ValidationError('Email and password must be provided')
        
        attrs['user'] = user
        return attrs
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=6, max_length=128)

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def validate_otp(self, value):
        email = self.initial_data.get('email')
        user = User.objects.get(email=email)
        if user.reset_password_token != value:
            raise serializers.ValidationError("Invalid OTP")
        return value

    def save(self):
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.reset_password_token = None
        user.save()
