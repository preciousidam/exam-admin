from rest_framework import serializers

from lessons.models import AdminNote, StudentNote

class AdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminNote
        fields='__all__'

class StudentNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentNote
        fields='__all__'
