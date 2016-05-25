from .settings import *

TESTS_IN_PROGRESS = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_db.sqlite3',
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DEBUG = False
TEMPLATE_DEBUG = False
