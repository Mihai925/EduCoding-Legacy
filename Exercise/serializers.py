from .models import Exercise
from rest_framework import serializers


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'content', 'classes_assigned_to', 'tests')