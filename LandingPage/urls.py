__author__ = 'varun'

from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    url(r'^\Z', HomePageView.as_view()),
]
