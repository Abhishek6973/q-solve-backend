from rest_framework import serializers
from .models import *

class createQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields= '__all__'

class responseQuestionSeializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields= '__all__'