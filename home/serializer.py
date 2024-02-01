from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['__all__']
        # exclude=['']
        
        # def validate(self,validated_data):
        #     if validated_data.get('title'):