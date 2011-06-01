import os

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/worldwide.db'
    }
}
INSTALLED_APPS = ['worldwide']

