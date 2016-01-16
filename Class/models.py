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


class Invitation(models.Model):
    invitation_id = models.AutoField("Invitation id", primary_key=True, blank=True)
    teacher = models.ForeignKey(User, related_name="Teacher")
    student_email = models.CharField("Student Email", max_length=100)
    invitation_code = models.CharField("Invitation Code", max_length=100)
    created_date = models.DateTimeField(auto_now=True, default=timezone.now)
    class_to_add = models.ForeignKey(Class, blank=True, null=True)

    class Meta:
        unique_together = (("invitation_code",),)