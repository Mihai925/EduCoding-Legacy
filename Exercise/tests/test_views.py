from django.test import TestCase
from django.test.utils import setup_test_environment
from mock import patch
from Exercise.views import get_exercise_for_student, student_single_exercise_editor
from Exercise.models import Exercise
from authentication.authenticate import register_student
from django.contrib.auth.models import Group
from django.test import Client
from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        Group.objects.get_or_create(name="Student")
        Group.objects.get_or_create(name="Teacher")
        register_student("Navi_Smailliw", "makingRussiaStrong", "vani@gmail.com", "Ivan", "Smailliw")

        setup_test_environment()

        self.client = Client()
        self.client.login(username="Navi_Smailliw", password="makingRussiaStrong")

    @patch('Exercise.views.get_assigned_exercise_for_students')
    def test_get_exercise_for_student(self, patch):
        patch.return_value = 'Dummy exercise'

        response = self.client.get(reverse(get_exercise_for_student))
        self.assertEqual(200, response.status_code)
        self.assertTrue('exercises' in response.context)
        self.assertEqual('Dummy exercise', response.context['exercises'])

    @patch('Exercise.views.Exercise.objects.get')
    def test_student_single_exercise_editor(self, patch):
        patch.return_value = Exercise.objects.create(description='Dummy description')

        response = self.client.get(reverse(student_single_exercise_editor, args=('1',)))

        self.assertEqual(200, response.status_code)
        self.assertTrue('ex_description' in response.context)
        self.assertEqual('Dummy description', response.context['ex_description'])
        patch.assert_called_with(ex_id='1')

    def test_compile_code(self):
        pass #TODO