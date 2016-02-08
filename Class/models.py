from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Class(models.Model):
    cls_id = models.AutoField("ClassManagement id", primary_key=True)
    teacher = models.ManyToManyField(User, related_name='teacher', blank=True)
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField('ClassManagement Name', max_length=100)
    description = models.CharField('ClassManagement Description', max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()