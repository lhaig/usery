from .base import *

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
