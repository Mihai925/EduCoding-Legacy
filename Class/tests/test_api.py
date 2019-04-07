from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.test import TestCase


class ClassApiTestCase(TestCase):
    fixtures = ['educoding/test_fixtures/test_fixture.json']

    def setUp(self):
        self.client = APIClient()

    def test_get_classes(self):
        user = User.objects.get(username='student')
        self.client.force_authenticate(user)
        response = self.client.get('/classes/', format='json')
        json_response = response.json()[0]
        self.assertEqual("Class1", json_response["name"])
        self.assertEqual(1, len(json_response["teacher"]))
        self.assertEqual(1, len(json_response["students"]))
