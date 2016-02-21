from django.conf.urls import url
from .views import TeacherRegistration

urlpatterns = [
    url(r'^register_teacher$', TeacherRegistration.as_view()),

]
