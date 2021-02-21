from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.permissions import *

from lessons.models import Lesson
from lessons.serializers import LessonSerializer

# Create your views here.

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or  self.action == 'list' :
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]