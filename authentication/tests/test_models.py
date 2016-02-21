from django.test import TestCase
from django.contrib.auth.models import User
from autofixture import AutoFixture
from authentication.models import Invitation


class InvitationsTestCase(TestCase):
    def test_invitation_creation(self):
        AutoFixture(User).create(10)
        user = User.objects.order_by('?').first()
        invitation = Invitation.objects.create(inviter=user, invitee_email="test@test.me")
        self.assertIsNotNone(invitation.invitation_code)
        # Check it's in the database, since we're overriding 'save'
        db_invite = Invitation.objects.get(inviter=user, invitee_email="test@test.me")
        self.assertEqual(invitation.invitation_code, db_invite.invitation_code)
