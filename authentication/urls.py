from django.conf.urls import url
from .views import TeacherRegistration, LoginView

urlpatterns = [
    url(r'^register_teacher^\Z', TeacherRegistration.as_view()),
    url(r'^login/^\Z', LoginView.as_view()),
]
