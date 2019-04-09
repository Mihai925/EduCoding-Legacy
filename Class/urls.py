from Class.api.views import ClassViewSet
from django.conf.urls import url, include
from rest_framework import routers
from .views import ClassManagementHomeView, ClassStudentsView, remove_student_from_class, \
    send_invites_to_students, create_new_class, delete_class, resend_invitation, delete_invitation

router = routers.DefaultRouter()
router.register(r'classes', ClassViewSet, base_name="classes")

urlpatterns = [
    url(r'^\Z', ClassManagementHomeView.as_view()),
    url(r'^get_students_in_class', ClassStudentsView.as_view()),
    url(r'^send_invitations', send_invites_to_students),
    url(r'^remove_user_from_class', remove_student_from_class),
    url(r'^create_class', create_new_class),
    url(r'^delete_class', delete_class),
    url(r'^resend_invite/(\d+)/^\Z', resend_invitation),
    url(r'^delete_invite/(\d+)/^\Z', delete_invitation)
]
