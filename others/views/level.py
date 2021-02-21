from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from others.serializers import LevelSerializer
from others.models import Level
from core.permissions import IsOwnerProfileOrReadOnly, IsAdminUser, IsLoggedInUserOrAdmin

# Create your views here.

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or  self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]