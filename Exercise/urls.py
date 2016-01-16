__author__ = 'varun'

from django.conf.urls import url
from .views import get_exercise_for_student, student_single_exercise_editor, submit_code, manage_exercise

urlpatterns = [
    url(r'^student/single_ex/(\d+)/$', student_single_exercise_editor, name="single_ex"),
    url(r'^student/submit', submit_code, name="submit"),
    url(r'^student', get_exercise_for_student, name="main_student_view"),
    url(r'^manage/$', manage_exercise, name="manage_exercises"),

]

