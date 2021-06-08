from rest_framework import serializers

from lessons.models import AdminNote, StudentNote
from harrp.models import StudentProfile

class AdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminNote
        fields='__all__'

class StudentNoteSerializer(serializers.ModelSerializer):
    shared_list = serializers.ListField(read_only=True)

    def update(self, instance, validated_data):
        shared = validated_data.pop('shared')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.visibility = validated_data.get('visibility', instance.visibility)
        instance.user = validated_data.get('user', instance.user)

        if instance.visibility == 0:
            instance.shared.clear()
        else:
            instance.shared.clear()
            instance.shared.add(*shared)
    
        instance.save()

        return instance


    class Meta:
        model=StudentNote
        fields='__all__'
        extra_kwargs = {'shared': {'allow_empty': True}}
