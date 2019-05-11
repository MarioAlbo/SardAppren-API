from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sardappren',
        'USER': 'sardappren',
        'PASSWORD': 'sardappren',
        'HOST': 'db',
        'PORT': '8010',
    }
}