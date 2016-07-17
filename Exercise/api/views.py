from rest_framework import viewsets

from Class.models import Class
from Exercise.api.serializers import ExerciseSerializer
from Exercise.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        """
        Gets all the exercises assigned to a particular student
        """
        user = self.request.user
        # Get all classes in which a student is, then get all the exs. assigned to
        # those classes
        return Exercise.objects.filter(classes_assigned_to__in=Class.objects.filter(students=user))
