__author__ = 'varun'

from django.conf.urls import url, include
from .views import AllExercisesView, SingleExerciseEditorView, submit_code, ManageExercisesView
from rest_framework import routers
from Exercise.api.views import ExerciseViewSet

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet, base_name="exercises")

urlpatterns = [
    url(r'^student/single_ex/(\d+)/\Z', SingleExerciseEditorView.as_view(), name="single_ex"),
    url(r'^student/submit/\Z', submit_code, name="submit"),
    url(r'^student/\Z', (AllExercisesView.as_view()), name="main_student_view"),
    url(r'^manage/\Z', ManageExercisesView.as_view(), name="manage_exercises")

]
