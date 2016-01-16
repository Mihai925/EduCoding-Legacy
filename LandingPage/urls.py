__author__ = 'varun'

from django.conf.urls import url
from .views import home_page, contact_us_form

urlpatterns = [
    url(r'^contact_us/$', contact_us_form),
    url(r'^$', home_page),
]
