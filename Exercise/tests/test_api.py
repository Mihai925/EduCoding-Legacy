from django.contrib.auth.models import User
from rest_framework.test import APIClient, force_authenticate
from django.test import TestCase


class ExerciseApiTestCase(TestCase):
    fixtures = ['educoding/test_fixtures/test_fixture.json']

    def setUp(self):
        self.client = APIClient()

    def test_get_exercises(self):
        user = User.objects.get(username='student')
        self.client.force_authenticate(user)
        response = self.client.get('/exercises/', format='json')
        json_response = response.json()[0]
        self.assertEqual("One exercise", json_response["title"])
        self.assertEqual(1, len(json_response["classes_assigned_to"]))
