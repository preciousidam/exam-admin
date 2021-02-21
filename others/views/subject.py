from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from others.serializers import SubjectSerializer, TopicSerializer
from others.models import Subject, Topic
from core.permissions import IsAdminUser, IsLoggedInUserOrAdmin

# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or  self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]



class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or  self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]