from django.db.models.base import Model
from rest_framework import serializers

from others.models import Subject, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):

    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model=Subject
        fields='__all__'