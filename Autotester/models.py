from django.db import models

# Create your models here.
class ExerciseTests(models.Model):
    input = models.CharField('Input', max_length=500)
    expected_output = models.CharField('Output', max_length=500)
