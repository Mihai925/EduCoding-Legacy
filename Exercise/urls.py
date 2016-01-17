__author__ = 'varun'

from django.conf.urls import url
from .views import AllExercisesView, SingleExerciseEditorView, submit_code, ManageExercisesView

urlpatterns = [
    url(r'^student/single_ex/(\d+)/$', SingleExerciseEditorView.as_view(), name="single_ex"),
    url(r'^student/submit', submit_code, name="submit"),
    url(r'^student', AllExercisesView.as_view(), name="main_student_view"),
    url(r'^manage/$', ManageExercisesView.as_view(), name="manage_exercises"),

]
