__author__ = 'varun'

from django.conf.urls import url
from .views import lessons_home_page, get_lesson_plan, get_create_new_lesson_page

urlpatterns = [
    url(r'^$', lessons_home_page),
    url(r'^get_lesson_plan/(\d+)/$', get_lesson_plan),
    url(r'^create_lesson_plan/$', get_create_new_lesson_page),
]

