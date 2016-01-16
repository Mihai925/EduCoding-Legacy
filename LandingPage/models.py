from django.db import models


class Feature(models.Model):
    title = models.CharField("Title", max_length=100, blank=False)
    description = models.TextField("Description", blank=False)
    icon = models.CharField("Glyphicon", max_length=100, blank=False)


class LandingPage(models.Model):
    description = models.TextField("Description", blank=False)
    features = models.ManyToManyField(Feature, related_name='Features', blank=False)
