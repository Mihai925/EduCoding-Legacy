from django.test import TestCase
from django.test import Client
from Exercise.models import Exercise


class ViewsTestCase(TestCase):
    fixtures = ['educoding/test_fixtures/test_fixture.json']

    def setUp(self):
        self.client = Client()

    #def test_single_exercise_editor_view(self):
    #    self.client.login(username="student", password="student")
    #    response = self.client.get('/Exercise/student/single_ex/1/')
    #    self.assertEquals(response.status_code, 200)
    #    self.assertIsInstance(response.context['form'], ExerciseForm)

    #def test_manage_exercises_view_get(self):
    #    self.client.login(username="teacher", password="teacher")
    #    response = self.client.get('/Exercise/manage/')
    #    self.assertEquals(response.status_code, 200)
    #    self.assertEquals(response.context['errors'], [])
    #    self.assertIsInstance(response.context['form'], NewExerciseForm)

    #def test_manage_exercises_view_post_happy_case(self):
    #    self.client.login(username="teacher", password="teacher")
    #    response = self.client.post("/Exercise/manage/", data={'inputTitle': 'title', 'inputDescription': 'description',
    #                                                           'code': 'code', 'input_test': ['a', 'b'],
    #                                                           'output_test': ['a', 'b']})
    #    self.assertEquals(response.status_code, 200)
    #    self.assertEquals(response.context['errors'], [])
    #    self.assertIsInstance(response.context['form'], NewExerciseForm)
    #    self.assertIsNotNone(Exercise.objects.get(title='title'))

    #def test_manage_exercises_view_post_errors(self):
    #    self.client.login(username="teacher", password="teacher")
    #    response = self.client.post("/Exercise/manage/", data={'code': 'code', 'input_test': ['a', 'b'],
    #                                                           'output_test': ['a', 'b']})
    #    self.assertEquals(response.status_code, 200)
    #    self.assertEquals(len(response.context['errors']), 2)