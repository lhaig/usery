from .base import *

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'widget_tweaks',
    'accounts',
    'portal',
]

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OPENSTACK_USERNAME = config('OPENSTACK_USERNAME')
OPENSTACK_PASSWORD = config('OPENSTACK_PASSWORD')
OPENSTACK_PROJECTNAME = config('OPENSTACK_PROJECTNAME')
OPENSTACK_AUTHURL = config('OPENSTACK_AUTHURL')
OPENSTACK_HORIZONURL= config('OPENSTACK_HORIZONURL')
OPENSTACK_SANDBOX_DOMAIN = config('OPENSTACK_SANDBOX_DOMAIN')
OPENSTACK_USER_DOMAIN_NAME = config('OPENSTACK_USER_DOMAIN_NAME')
OPENSTACK_PROJECT_DOMAIN_NAME = config('OPENSTACK_PROJECT_DOMAIN_NAME')
FROM_EMAIL = config('FROM_EMAIL')
SUPPORT_EMAIL= config('SUPPORT_EMAIL')
