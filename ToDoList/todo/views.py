from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django.core import serializers
from .models import ToDo
from .serializers import ToDoSerializer
from django.http import HttpResponse


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def Create(self, request):
        todo = ToDo.objects.create(title=request.POST.get('title', ''), description=request.POST.get('description', ''), user=request.user)
        serializer_obj = serializer.serialize('json', [todo, ])
        return HttpResponse(serializer_obj)