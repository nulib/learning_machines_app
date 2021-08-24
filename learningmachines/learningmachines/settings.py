"""
Django settings for learningmachines project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from .credentials import DJANGO_SECRET, DEV_DB_PROFILE, AWS_PROFILE, S3_OBJECT, EMAIL_INFO, DB_ENV
import os
import sys
import boto3

import mimetypes
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/js", ".js", True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True#not S3_OBJECT['USE_S3']

ALLOWED_HOSTS = ['3.19.31.134', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'searcher'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learningmachines.urls'
#['/Users/ezraedgerton/Desktop/projects/learningmachines_folder/venv3_8/lib/python3.8/site-packages/django']

print(os.path.join(BASE_DIR, 'templates'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'searcher','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learningmachines.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DB_ENV == 'LOCAL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'TEST': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            },
        }
    }
if DB_ENV == 'PRODUCTION':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'dev_db',                 # Or path to database file if using sqlite3.
            'USER': DEV_DB_PROFILE['user'],       # Not used with sqlite3.
            'PASSWORD': DEV_DB_PROFILE['password'],      # Not used with sqlite3.
            #'HOST': 'mellondb-dev.cykdbek7llhv.us-east-2.rds.amazonaws.com',          
            'HOST': 'mellon-db-01.cykdbek7llhv.us-east-2.rds.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',       # Set to empty string for default. Not used with sqlite3.
        }
    }
if DB_ENV == 'DEV':
    RDS_ENDPOINT="mellondb-dev.cykdbek7llhv.us-east-2.rds.amazonaws.com"
    RDS_PORT="5432"
    RDS_USR="zhaowezra"
    RDS_REGION="us-east-2"
    RDS_DBNAME="dev_db"

    session = boto3.Session()
    client = session.client('rds', region_name=RDS_REGION)

    token = client.generate_db_auth_token(DBHostname=RDS_ENDPOINT, Port=RDS_PORT, DBUsername=RDS_USR, Region=RDS_REGION)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': RDS_DBNAME,       # Or path to database file if using sqlite3.
            'USER': RDS_USR,                      # Not used with sqlite3.
            'PASSWORD': token,          # Not used with sqlite3.
            'HOST': RDS_ENDPOINT,                 # Set to empty string for localhost. Not used with sqlite3.
            'PORT': RDS_PORT,    
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL  = 'Learning Machines App <noreply@learningmachines.com>'
EMAIL_HOST_USER = EMAIL_INFO['EMAIL_NAME']
EMAIL_HOST_PASSWORD = EMAIL_INFO['EMAIL_PW']




# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
USE_S3 = S3_OBJECT['USE_S3']

REDIS_IP = '18.118.158.133' if USE_S3 else 'localhost'
REDIS_URL='redis://'+ REDIS_IP +':6379'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = AWS_PROFILE['ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = AWS_PROFILE['SECRET_KEY']
    AWS_STORAGE_BUCKET_NAME = S3_OBJECT['BUCKET_NAME']
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    print(STATIC_URL)
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = 'static'
    
