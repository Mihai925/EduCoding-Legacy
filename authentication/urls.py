__author__ = 'varun'

from django.conf.urls import url
from .views import login, logout, register_student, check_username, authentication_page, subscribe_user, \
    register_student_page, automatic_login_student, automatic_login_teacher, check_email

urlpatterns = [
    url(r'^$', authentication_page),
    url(r'^login_as_student/d0785afd1fec4768953cb7ee0e80da14/$', automatic_login_student),
    url(r'^login_as_teacher/5818f995280e4e4f9d847b7c40fe2109/$', automatic_login_teacher),
    url(r'^logout', logout),
    url(r'^login', login),
    url(r'^register/student/$', register_student),
    url(r'^check-username', check_username),
    url(r'^check-email/$', check_email),
    url(r'^register/student/(\w+)/$', register_student_page),
    url(r'^subscribe', subscribe_user),
]
