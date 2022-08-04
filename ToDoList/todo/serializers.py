from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at', 'user'] #, 'user'
