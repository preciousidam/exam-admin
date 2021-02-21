from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.permissions import *

from lessons.models import AdminNote, StudentNote
from lessons.serializers import AdminNoteSerializer, StudentNoteSerializer

# Create your views here.

class AdminNoteViewSet(viewsets.ModelViewSet):
    queryset = AdminNote.objects.all()
    serializer_class = AdminNoteSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or  self.action == 'list' :
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]


class StudentNoteViewSet(viewsets.ModelViewSet):
    queryset = StudentNote.objects.all()
    serializer_class = StudentNoteSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsOwnerProfileOrReadOnly]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerProfileOrReadOnly]
        elif self.action == 'retrieve' or  self.action == 'list' :
            permission_classes = [IsOwnerProfileOrReadOnly]
        return [permission() for permission in permission_classes]