from . import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="django-insecure-1t8su@%v5nr")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Alloweb hosts. *
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default='*')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("POSTGRES_HOST"),
        'PORT': env.str("POSTGRES_PORT"),
    }
}

# CorsHeader
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", default=False)
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=('http://127.0.0.1:3000',
                                                                   'http://localhost:3000',
                                                                   'http://0.0.0.0:3000',))
CSRF_TRUSTED_ORIGINS = ('http://localhost:8000',)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
