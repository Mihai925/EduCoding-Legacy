__author__ = 'varun'

from logentries import LogentriesHandler
import os
import logging

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'codeaton_dev',
        'USER': 'codeaton_dev',
        'PASSWORD': '6nV-trE-5xZ-ger',
        'HOST': 'codeaton-dev.cixo4mjprn2r.us-west-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}

SUBCRIPTION_SPREADSHEET_KEY = '1kz40sKd0w1LdsmjxQqi2ioYf7r4mVAtuvz-Dk40IHVE'
SUBCRIPTION_WORKSHEET_KEY = 'od6'

URL = "http://test-dev.codeaton.com"

SMTP_SERVER = "email-smtp.us-east-1.amazonaws.com"
SMTP_SERVER_PORT = 587
SMTP_USERNAME = "AKIAIJUZK5T7YN4GMIXQ"
SMTP_PASSWORD = "AgbbsdsNQpvAPxyZCviQBTPaJdP2e46M8wSJxOjldacU"
SMTP_FROM_EMAIL = "support@codeaton.com"
USE_LANDING_PAGE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.dirname(os.path.abspath(__file__)) + "/../logs/log.log",
            'maxBytes': 5000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'logentries_handler': {
            'token': 'a1658621-8394-430a-898e-855194003ba5',
            'class': 'logentries.LogentriesHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile', 'logentries_handler'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console', 'logfile', 'logentries_handler'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
