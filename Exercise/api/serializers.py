from Exercise.models import Exercise
from rest_framework import serializers


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'content', 'classes_assigned_to', 'tests')
        depth = 1
