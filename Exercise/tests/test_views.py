from django.test import TestCase
from django.test import Client
from Exercise.models import Exercise
from ..forms import NewExerciseForm, ExerciseForm


class ViewsTestCase(TestCase):
    fixtures = ['educoding/test_fixtures/test_fixture.json']

    def setUp(self):
        self.client = Client()

    def test_single_exercise_editor_view(self):
        self.client.login(username="student", password="student")
        response = self.client.get('/Exercise/student/single_ex/1/')
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ExerciseForm)

    def test_all_exercises_view(self):
        self.client.login(username="student", password="student")
        response = self.client.get('/Exercise/student/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['name'], "Jon")
        self.assertEquals(len(response.context['exercises']), 1)
        self.assertEquals(response.context['exercises'][0][1][0].ex_id, 1)

    def test_manage_exercises_view_get(self):
        self.client.login(username="teacher", password="teacher")
        response = self.client.get('/Exercise/manage/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['errors'], [])
        self.assertIsInstance(response.context['form'], NewExerciseForm)

    def test_manage_exercises_view_post_happy_case(self):
        self.client.login(username="teacher", password="teacher")
        response = self.client.post("/Exercise/manage/", data={'inputTitle': 'title', 'inputDescription': 'description',
                                                               'code': 'code', 'input_test': ['a', 'b'],
                                                               'output_test': ['a', 'b']})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['errors'], [])
        self.assertIsInstance(response.context['form'], NewExerciseForm)
        self.assertIsNotNone(Exercise.objects.get(title='title'))

    #def test_manage_exercises_view_post_errors(self):
    #    self.client.login(username="teacher", password="teacher")
    #    response = self.client.post("/Exercise/manage/", data={'code': 'code', 'input_test': ['a', 'b'],
    #                                                           'output_test': ['a', 'b']})
    #    self.assertEquals(response.status_code, 200)
    #    self.assertEquals(len(response.context['errors']), 2)