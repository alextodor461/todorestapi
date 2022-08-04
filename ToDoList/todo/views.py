from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from todo.serializers import ToDoSerializer
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = ToDoSerializer
    #permission_classes = [] #permissions.IsAuthenticated