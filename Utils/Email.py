__author__ = 'varun'

from codeaton.settings import SMTP_FROM_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT, SMTP_USERNAME
import smtplib
import logging

LOGGER = logging.getLogger(__name__)


class Email:
    def __init__(self, to_address=None, message=None, subject="Code-A-Ton"):
        self.to_address = to_address
        self.message = message
        self.subject = subject

    def send(self):
        server = smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT)
        LOGGER.info(server.starttls())
        LOGGER.info(server.login(SMTP_USERNAME, SMTP_PASSWORD))
        LOGGER.info("Sending Email to: " + self.to_address)
        try:
            LOGGER.info(server.sendmail(SMTP_FROM_EMAIL, self.to_address,
                                        'Subject: %s\n\n%s' % (self.subject, str(self.message))))
        except Exception as e:
            LOGGER.error(e)
            return False
        LOGGER.info(server.close())
        return True