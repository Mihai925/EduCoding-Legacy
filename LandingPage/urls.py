__author__ = 'varun'

from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]
