from django.db.models import fields
from rest_framework import serializers

from harrp.models import User, StudentProfile, School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=['id','name']

class StudentProfileSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True, read_only=True)
    class Meta:
        model=StudentProfile
        fields='__all__'
        extra_kwargs = {'user': {'write_only': True}}
        


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = StudentProfileSerializer(read_only=True)
    class Meta:
        model=User
        fields= ['url','email', 'password', 'first_name', 'last_name', 'phone', 'pk', 'verified', 'profile' ]
        extra_kwargs = {'password': {'write_only': True}, 'verified': {'read_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User(is_staff=False, is_superuser=False, is_active=True, email=email.lower(), **validated_data)
        user.set_password(password)
        user.save()
        return user

