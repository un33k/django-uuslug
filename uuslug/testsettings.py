import os

DEBUG = TEMPLATE_DEBUG = True

PROJECT_NAME = "uuslug"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_NAME.strip().split(".")[0]+"_db"
    }
}
INSTALLED_APPS = [
    'uuslug',
]


