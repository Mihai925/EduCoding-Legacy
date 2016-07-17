from Class.models import Class
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name', 'description', 'teacher', 'students', 'exercise_set')
        depth = 1
