import os

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/uuslug.db'
    }
}
INSTALLED_APPS = ['uuslug']

