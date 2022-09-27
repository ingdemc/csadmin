from .base import *
DEBUG = True

ALLOWED_HOSTS = ['cs--admin.herokuapp.com']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'decfdv3aaoot8e',
        'USER': 'czpkfildxspopq',
        'PASSWORD': 'c9e223395cf5f5a327150be4df21fa3b2ad56a350b7ed1573b5f230707bc8ddb',
        'HOST': 'ec2-34-197-84-74.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
    }

    

}
