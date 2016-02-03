from django.db import models


class Feature(models.Model):
    title = models.CharField("Title", max_length=100, blank=False)
    description = models.TextField("Description", blank=False)
    icon = models.CharField("Glyphicon", max_length=100, blank=False)


class Quotes(models.Model):
    author = models.CharField("Author", max_length=100, blank=False)
    text = models.TextField("Text", blank=False)
    picture = models.ImageField("Picture", upload_to="author_pictures/")


class LandingPage(models.Model):
    description = models.TextField("Description", blank=False)
    quotes = models.ManyToManyField(Quotes, related_name='Quptes', blank=False)
    features = models.ManyToManyField(Feature, related_name='Features', blank=False)

    @property
    def get_features(self):
        return self.features.all()