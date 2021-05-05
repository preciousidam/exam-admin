from django.db.models.base import Model
from rest_framework import serializers

from others.models import Subject, Topic
from exercises.serializers import ExerciseSerializer
from lessons.serializers import AdminNoteSerializer, LessonSerializer, lesson

class TopicSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)
    lessons = LessonSerializer(many=True)
    subject_title = serializers.CharField()
    adminnote_notes = AdminNoteSerializer(many=True)
    class Meta:
        model=Topic
        fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):

    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model=Subject
        fields='__all__'