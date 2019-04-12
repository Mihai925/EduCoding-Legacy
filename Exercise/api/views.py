from rest_framework import viewsets

from Exercise.api.serializers import ExerciseSerializer
from Exercise.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        user = self.request.user
        return Exercise.objects.filter(author=user)