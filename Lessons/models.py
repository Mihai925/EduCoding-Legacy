from django.db import models

from Exercise.models import Exercise


# Lesson model
class Lesson(models.Model):
    lesson_id = models.AutoField('Lesson ID', primary_key=True)
    title = models.CharField('Lesson Title', max_length=100, blank=False)
    description = models.CharField('Lesson Description', max_length=100, blank=False, default="")
    briefing = models.TextField('Briefing', blank=False, default="")
    introduction = models.TextField('Introduction', blank=False, default="")
    assignments = models.ManyToManyField(Exercise, blank=True)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.title


class Unit(models.Model):
    unit_id = models.AutoField('Unit ID', primary_key=True)
    title = models.CharField('Unit Title', max_length=100, blank=False)
    lessons = models.ManyToManyField(Lesson, blank=True)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.title

