from rest_framework import serializers

from lessons.models import Lesson, Paragraph, FeaturedImage
from others.models import Subject, Topic



class FeaturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeaturedImage
        fields="__all__"


class ParagraphSerializer(serializers.ModelSerializer):
    images = FeaturedImageSerializer(many=True)
    class Meta:
        model=Paragraph
        fields='__all__'


class LessonSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True)
    class Meta:
        model=Lesson
        fields='__all__'