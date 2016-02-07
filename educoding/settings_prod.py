__author__ = 'varun'

import os

SUBCRIPTION_SPREADSHEET_KEY = '1HUjusmHI41AbmrvcUkh_8gs-Z3kMKWSJopS1B_Z-BQM'
SUBCRIPTION_WORKSHEET_KEY = 'od6'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'educoding',
        'USER': 'educoding',
        'PASSWORD': '6nV-trE-5xZ-ger',
        'HOST': 'educoding-db.cixo4mjprn2r.us-west-2.rds.amazonaws.com',
        'PORT': '5432'
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
        'logentries_handler': {
            'token': '88660975-3df8-41b7-a451-5d060d550dfa',
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
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

URL = "http://www.educoding.co"
SMTP_SERVER = "email-smtp.us-east-1.amazonaws.com"
SMTP_SERVER_PORT = 587
SMTP_USERNAME = "AKIAIJUZK5T7YN4GMIXQ"
SMTP_PASSWORD = "AgbbsdsNQpvAPxyZCviQBTPaJdP2e46M8wSJxOjldacU"
SMTP_FROM_EMAIL = "support@educoding.com"
USE_LANDING_PAGE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False