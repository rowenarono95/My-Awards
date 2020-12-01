 
from rest_framework import serializers
from .models import *
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'image', 'description', 'date_created', 'link','user')
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'profile_pic', 'bio', 'user', 'link')
