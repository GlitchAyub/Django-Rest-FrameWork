from rest_framework import serializers
from .models import *
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['title']
        # exclude=['description']
        
 # if you want to validate only single field 
    def get_slug(self,obj):
        return slugify(obj.title)
    # def validate_title(self, data):
    #     title = data
        
    #     if title:
    #         regex = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[\w\d]{8,}$')
            
    #         if not regex.search(title):
    #             raise serializers.ValidationError('Title cannot contain special characters')
        
    #     return data
        
    def validate(self, validated_data):
        title = validated_data.get('title')
        
        if title:
            regex = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[\w\d]{8,}$')
            
            if not regex.search(title):
                raise serializers.ValidationError('Title cannot contain special characters')
        
        return validated_data
    
 
