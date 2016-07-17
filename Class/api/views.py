from rest_framework import viewsets

from Class.api.serializers import ClassSerializer
from Class.models import Class


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer

    def get_queryset(self):
        """
        Get all classes for a specific student
        """
        user = self.request.user
        return Class.objects.filter(students=user)
