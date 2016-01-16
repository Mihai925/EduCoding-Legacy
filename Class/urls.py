__author__ = 'varun'

from django.conf.urls import url
from .views import class_management_home_page, get_student_for_class, remove_student_from_class, \
    send_invites_to_students, create_new_class, delete_class, resend_invitation, delete_invitation

urlpatterns = [
    url(r'^$', class_management_home_page),
    url(r'^get_students_in_class', get_student_for_class),
    url(r'^send_invitations', send_invites_to_students),
    url(r'^remove_user_from_class', remove_student_from_class),
    url(r'^create_class', create_new_class),
    url(r'^delete_class', delete_class),
    url(r'^resend_invite/(\d+)/$', resend_invitation),
    url(r'^delete_invite/(\d+)/$', delete_invitation),
]

