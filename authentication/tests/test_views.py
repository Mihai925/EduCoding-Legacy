from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.test.utils import setup_test_environment

from autofixture import AutoFixture

from authentication.authenticate import TestClient
from authentication.models import Invitation


class TeacherRegistrationTestCase(TestCase):

    def setUp(self):
        setup_test_environment()
        self.invitation = AutoFixture(Invitation, generate_fk=True).create(1)[0]
        self.user = AutoFixture(User).create(1)[0]
        self.client = TestClient()

    def test_no_invitation_code(self):
        response = self.client.get('/register_teacher')
        self.assertEqual(response.status_code, 302)

    def test_invitation_code_not_found(self):
        wrong_invitation_code = "ABCD"
        response = self.client.get('/register_teacher', {'invitation_code': wrong_invitation_code})
        self.assertEqual(response.status_code, 302)

    def test_registration_for_loggedin_user(self):
        self.client.login_user(self.user)
        response = self.client.get('/register_teacher', {'invitation_code': self.invitation.invitation_code})
        self.assertEqual(response.status_code, 302)

    def test_legitimate_invitee(self):
        response = self.client.get('/register_teacher', {'invitation_code': self.invitation.invitation_code})
        self.assertEqual(response.status_code, 200)

    def test_teacher_registration(self):
        invitation_code = AutoFixture(Invitation, generate_fk=True).create(1)[0].invitation_code
        response = self.client.post('/register_teacher', {'username': 'test@test.me', 'password': 'Test12345',
                                                          'first_name': 'Johnny', 'last_name': 'Bravo',
                                                          'invitation_code': invitation_code})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='test@test.me')
        self.assertEqual(user.email, 'test@test.me')
        self.assertTrue(user.groups.filter(name='Teacher').exists())
        #self.assertFalse(Invitation.objects.filter(invitation_code=invitation_code).exists()) TODO
