"""
Development settings
"""
from os.path import join, normpath, dirname

import debug_toolbar

from common import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# debug_toolbar settings
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS += (join(dirname(debug_toolbar.__file__), 'templates'),)
STATICFILES_DIRS += (join(dirname(debug_toolbar.__file__), 'static'),)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

THIRD_PARTY_APPS += (
    'debug_toolbar',
)
