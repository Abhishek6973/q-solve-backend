from rest_framework import serializers
from .models import *

class createKitSerializer(serializers.ModelSerializer):
    class Meta:
        model=KitModel
        fields= '__all__'