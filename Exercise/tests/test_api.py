from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.test import TestCase


class ExerciseApiTestCase(TestCase):
    fixtures = ['educoding/test_fixtures/test_fixture.json']

    def setUp(self):
        self.client = APIClient()

    def test_get_exercises_by_user(self):
        user = User.objects.get(username='admin')
        self.client.force_authenticate(user)
        response = self.client.get('/api/exercises/', format='json')
        json_response = response.json()[0]
        self.assertEqual("One exercise", json_response["title"])
        self.assertEqual(True, json_response["has_tests"])
        self.assertEqual("C++", json_response["language"])

    def test_get_specific_exercise(self):
        user = User.objects.get(username='admin')
        self.client.force_authenticate(user)
        response = self.client.get('/api/exercises/1/', format='json')
        json_response = response.json()
        self.assertEqual("One exercise", json_response["title"])
        self.assertEqual(True, json_response["has_tests"])
        self.assertEqual("C++", json_response["language"])

    def test_put_exercise(self):
        user = User.objects.get(username='admin')
        self.client.force_authenticate(user)
        response = self.client.put('/api/exercises/2/', {
            "ex_id": 2,
            "author": 1,
            "title": "Test exercise 2",
            "description": "Test exercise 3",
            "content": "print 'Hello'",
            "has_tests": False,
            "language": "Python",
            "tests": []
            }, format='json')
        self.assertEquals(response.status_code, 200)

    def test_post_exercise(self):
        user = User.objects.get(username='admin')
        self.client.force_authenticate(user)
        response = self.client.post('/api/exercises/', {
            "title": "Test exercise 4",
            "description": "Test exercise 4",
            "content": "print 'Hello'",
            "has_tests": True,
            "language": "Python",
            "tests": []
            }, format='json')
        self.assertEquals(response.status_code, 201)