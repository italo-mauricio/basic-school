from rest_framework import serializers
from .models import Course, Avaliable


class AvaliableSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliable
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comentary',
            'avaliable',
            'create',
            'active'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'tittle',
            'url',
            'created',
            'active'
        )