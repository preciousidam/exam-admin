from rest_framework import serializers

from others.models import Level

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields='__all__'
        extra_kwargs={'subject': {'read_only': True}, 'level_name': {'read_only': True}}