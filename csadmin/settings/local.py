from .base import *
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'csadmin',
        'USER': 'postgres',
        'PASSWORD': 'i076117',
        'HOST': 'localhost',
        'DATABASE_PORT':'5432',
    }

    

}
