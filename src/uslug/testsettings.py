import os

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/uslug.db'
    }
}
INSTALLED_APPS = ['uslug']

