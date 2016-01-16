__author__ = 'varun'

from django.conf.urls import url
from .views import teacher_home_calender_page

urlpatterns = [
    url(r'^$', teacher_home_calender_page),
]
