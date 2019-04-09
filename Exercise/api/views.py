from rest_framework import viewsets

from Exercise.api.serializers import ExerciseSerializer
from Exercise.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()