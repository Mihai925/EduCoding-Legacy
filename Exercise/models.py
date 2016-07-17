from django.db import models
from Autotester.models import ExerciseTests

from Class.models import Class


# Exercise models.
class Exercise(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100, blank=False)
    description = models.TextField('Description', blank=False)
    content = models.TextField('Content', blank=False)
    classes_assigned_to = models.ManyToManyField(Class, blank=True)
    tests = models.ManyToManyField(ExerciseTests, blank=True)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.title


