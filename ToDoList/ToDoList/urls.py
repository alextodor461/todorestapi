from django.contrib import admin
from django.urls import path, include
from todo.views import ToDoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
