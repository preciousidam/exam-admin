from rest_framework import serializers
from harrp.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'
        extra_kwargs = {'students': {'read_only': True}}