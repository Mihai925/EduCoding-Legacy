from django.db import models
from django.contrib.auth.models import User
import random
import string


class Invitation(models.Model):
    inviter = models.ForeignKey(User)
    invitee_email = models.EmailField()
    invitation_code = models.CharField(max_length=5, unique=True)

    def save(self, *args, **kwargs):
        self.invitation_code = ''.join(random.SystemRandom()
                                      .choice(string.ascii_uppercase + string.digits) for _ in range(5))
        super(Invitation, self).save(*args, **kwargs)
