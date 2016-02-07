__author__ = 'varun'

import os
import sys

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'/tmp/database.db',
        'TEST_NAME':'/tmp/database_test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}


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
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
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

SUBCRIPTION_SPREADSHEET_KEY = '1kz40sKd0w1LdsmjxQqi2ioYf7r4mVAtuvz-Dk40IHVE'
SUBCRIPTION_WORKSHEET_KEY = 'od6'

URL = "http://127.0.0.1:8000"

SMTP_SERVER = "email-smtp.us-east-1.amazonaws.com"
SMTP_SERVER_PORT = 587
SMTP_USERNAME = "AKIAIJUZK5T7YN4GMIXQ"
SMTP_PASSWORD = "AgbbsdsNQpvAPxyZCviQBTPaJdP2e46M8wSJxOjldacU"
SMTP_FROM_EMAIL = "support@codeaton.com"
USE_LANDING_PAGE = True
COMPILER_API = "http://127.0.0.1:8089/compile"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
