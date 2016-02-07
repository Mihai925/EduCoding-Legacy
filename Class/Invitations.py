__author__ = 'varun'

from educoding.settings import URL
from .models import Invitation as InvitationModel
from django.template import Context
from django.template.loader import get_template
from educoding.settings import SMTP_FROM_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT, SMTP_USERNAME
import uuid
import smtplib
import threading
import logging
from django.contrib.auth.models import User
from .models import Class
from Utils.Email import Email

LOGGER = logging.getLogger(__name__)


def send_invites(emails, teacher, class_id):
    invitations = []
    class_to_add_to = Class.objects.get(cls_id=class_id)
    for email in emails:
        existing_users = list((User.objects.filter(email=email)))
        if len(existing_users) == 0:
            invitation = Invitation(teacher=teacher, email=email, class_to_add_to=class_to_add_to)
            invitation.save_invitation()
            invitations.append(invitation)
        else:
            class_to_add_to.students.add(existing_users[0])
            class_to_add_to.save()
    invitations_thread = SendInvitationsEmails(invitations)
    invitations_thread.start()
    return True


class SendInvitationsEmails(threading.Thread):
    def __init__(self, invitations):
        super(SendInvitationsEmails, self).__init__()
        self.invitations = invitations

    def run(self):
        for i in self.invitations:
            i.email_invitation()


class Invitation:
    def __init__(self, teacher=None, email=None, invitation_code=None, class_to_add_to=None, invitation_id=None):
        if teacher is not None and email is not None:
            self.teacher = teacher
            self.email = email
            self.class_to_add_to = class_to_add_to
            self.invitation_code = uuid.uuid4().hex
            while len(list(InvitationModel.objects.filter(invitation_code=self.invitation_code))) != 0:
                self.invitation_code = uuid.uuid4().hex
        elif invitation_code is not None:
            self.invitation_code = invitation_code
            invitation = InvitationModel.objects.get(invitation_code=invitation_code)
            if invitation is None:
                raise InvalidInvitationCodeException(
                    "This invitation code is invalid. Please speak to your teacher who sent you invitation.")
            self.teacher = invitation.teacher
            self.email = invitation.student_email
            self.class_to_add_to = invitation.class_to_add
        elif invitation_id is not None:
            invitation = InvitationModel.objects.get(invitation_id=invitation_id)
            if invitation is None:
                raise InvalidInvitationCodeException(
                    "This invitation code is invalid. Please speak to your teacher who sent you invitation.")
            self.teacher = invitation.teacher
            self.email = invitation.student_email
            self.class_to_add_to = invitation.class_to_add
            self.invitation_code = invitation.invitation_code
        else:
            raise InvalidInvitationConstructionException("Please use correct construction for Invitation")

    def get_hash_code(self):
        return self.invitation_code

    def email_invitation(self):
        text = get_template("class_management/email.html").render(
            Context({
                'URL': self.__get_invitation_registration_url(),
                'teacher_name': self.teacher.first_name,
            }))
        try:
            email = Email(to_address=self.email, message=text, subject="Invitation to Join Code-A-Ton")
            email.send()
            return True
        except Exception as e:
            LOGGER.error(e)
            return False

    def save_invitation(self):
        invite = InvitationModel()
        invite.teacher = self.teacher
        invite.student_email = self.email
        invite.invitation_code = self.invitation_code
        invite.class_to_add = self.class_to_add_to
        invite.save()

    def add_student_to_class(self):
        self.class_to_add_to.students.add(User.objects.filter(email=self.email)[0])
        self.class_to_add_to.save()

    def __get_invitation_registration_url(self):
        return URL + "/authentication/register/student/" + self.invitation_code + "/"

    def remove_invitation(self):
        invitation = InvitationModel.objects.get(invitation_code=self.invitation_code)
        if invitation is not None:
            invitation.delete()
        else:
            raise InvalidInvitationCodeException("This invitation does not exist.")


def send_invitation_email(invitation_id, teacher):
    invitation = Invitation(invitation_id=invitation_id)
    if invitation is not None and invitation.teacher == teacher:
        SendInvitationsEmails(invitations=[invitation]).run()
        return True
    return False


def delete_invitation(invitation_id, teacher):
    invitation = Invitation(invitation_id=invitation_id)
    print invitation.teacher.username
    print teacher.username
    if invitation is not None and invitation.teacher == teacher:
        invitation.remove_invitation()
        return True
    return False


class InvalidInvitationCodeException(Exception):
    def __init__(self, message):
        super(InvalidInvitationCodeException, self).__init__(message)
        self.message = message


class InvalidInvitationConstructionException(Exception):
    def __init__(self, message):
        super(InvalidInvitationConstructionException, self).__init__(message)
        self.message = message
