import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY', 'tralalalala')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'authentication',
    'Panel',
    'Exercise',
    'Compiler',
    'Class',
    "Utils",

    'LandingPage',
    'Autotester',

    #3rd Party
    'django_ace',
    'widget_tweaks',
    'selectable',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'educoding.urls'

WSGI_APPLICATION = 'educoding.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, '')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'), )
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATES = [
 {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            "django.contrib.auth.context_processors.auth",
            "django.template.context_processors.debug",
            "django.template.context_processors.i18n",
            "django.template.context_processors.media",
            "django.template.context_processors.static",
            "django.template.context_processors.tz",
            "django.contrib.messages.context_processors.messages",
            'django.template.context_processors.csrf',
            "django.template.context_processors.request",
        ],
    },
},
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

AUTH_PROFILE_MODULE = "model.models.UserProfile"



LOGIN_URL = "/"
LOGOUT_URL = "/authentication/logout"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
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
            'class': 'logging.NullHandler',
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

#E-mail setup for SES:

COMPILER_API = os.environ.get('COMPILER_API', '')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
SOUTH_TESTS_MIGRATE = False

#Things I need to get rid of (currently needed for legacy resons):

SUBCRIPTION_SPREADSHEET_KEY = 'mock'
SUBCRIPTION_WORKSHEET_KEY = 'mock'
SMTP_SERVER = "mock"
SMTP_SERVER_PORT = 587
SMTP_USERNAME = "mock"
SMTP_PASSWORD = "mock"
SMTP_FROM_EMAIL = "mock"
GOOGLE_DRIVE_USERNAME = "mock"
GOOGLE_DRIVE_PASSWORD = "mock"
GOOGLE_DRIVE_FOLDER_KEY = 'mock'
HELLO_EMAIL = "mock"
GOOGLE_DRIVE_USERNAME = "mock"
GOOGLE_DRIVE_PASSWORD = "mock"
GOOGLE_DRIVE_FOLDER_KEY = 'mock'
HELLO_EMAIL = "mock"