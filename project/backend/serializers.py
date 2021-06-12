from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['name', 'owner', 'tasks']
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    lists = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'lists']
    