from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q

from core.permissions import *

from lessons.models import AdminNote, StudentNote
from lessons.serializers import AdminNoteSerializer, StudentNoteSerializer
from harrp.models import User

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

    def create(self, request, *args, **kwargs):

        
        shared = []

        if len(request.data.get('shared')) > 0:
            for email in request.data.get('shared'):
                student = User.objects.get(email=email.lower())
                if (student):
                    shared.append(student.id)

        request.data.update({'shared': shared})


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):

        shared = []
    
        if len(request.data.get('shared')) > 0:
            for email in request.data.get('shared'):
                student = User.objects.get(email=email.lower())
                if (student):
                    shared.append(student.id)

        request.data.update({'shared': shared})
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def list(self, request):
        student = request.query_params.get("student")

        if student == None:
            notes = StudentNote.objects.all()
            
        else:
            notes = StudentNote.objects.filter(Q(user=student) | Q(shared__in=[student])).all()

        serializer = self.get_serializer(notes, many=True)

        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'destroy':
            permission_classes = [IsOwnerProfileOrReadOnly]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerProfileOrReadOnly]
        elif self.action == 'retrieve' or  self.action == 'list' :
            permission_classes = [IsOwnerProfileOrReadOnly]
        return [permission() for permission in permission_classes]