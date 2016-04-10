from .models import ExerciseTests
from rest_framework import serializers


class ExerciseTestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExerciseTests
        fields = ('input', 'expected_output')