from django.db import models
from django.contrib.auth.models import User

from Class.models import Class

SUPPORTED_PROGRAMMING_LANGUAGES = (
    ("C++", "C++"),
    ("Python", "Python")
)


class ExerciseTests(models.Model):
    input = models.CharField('Input', max_length=500, blank=True)
    expected_output = models.CharField('Output', max_length=500, blank=True)


class Exercise(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100, blank=False)
    description = models.TextField('Description', blank=False)
    content = models.TextField('Content', blank=False)
    classes_assigned_to = models.ManyToManyField(Class, blank=True)
    has_tests = models.BooleanField("Has tests", default=False)
    tests = models.ManyToManyField(ExerciseTests, blank=True)
    language = models.CharField(choices=SUPPORTED_PROGRAMMING_LANGUAGES, default="cpp", max_length=20)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.title