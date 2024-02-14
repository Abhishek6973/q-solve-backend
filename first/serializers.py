from rest_framework import serializers
from .models import User,Question

msg = "Token is not Valid or Expired"

class UserRegistrationSerializer(serializers.ModelSerializer ):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["email", "name", "phone_num", "password", "password2","about_me", "website_link", "twitter_link", "github_link", "phone_num", "experience_level"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password don't match" )
        
        return attrs
    def create(self, validated_data):
        validated_data.pop("password2", None)
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
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Email and password must be provided')

        attrs['user'] = user
        return attrs