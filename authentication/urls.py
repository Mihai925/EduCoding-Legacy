from django.conf.urls import url
from .views import TeacherRegistration, LoginView

urlpatterns = [
    url(r'^register_teacher$', TeacherRegistration.as_view()),
    url(r'^login/$', LoginView.as_view()),
]
