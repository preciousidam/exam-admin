"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','rr-29m-%ytb29n_f^d298k_!=f%s!@a!k_w9w732(ju6k%yd0e')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'nested_admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'ckeditor',
    'rest_framework_simplejwt',
    'harrp.apps.HarrpConfig',
    'mailer',
    'others',
    'lessons',
    'exercises',
    'subscription',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Bangui'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR/"staticfiles"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
GRAPPELLI_ADMIN_TITLE= 'Harrp Admin'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'harrp.serializers.UserSerializer'
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'harrp-app'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=366),
}

AUTH_USER_MODEL = 'harrp.User'

SITE_ID = 1

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME',''),
    'API_KEY': os.environ.get('CLOUD_API_KEY',''),
    'API_SECRET': os.environ.get('CLOUD_API_SECRET',''),
    'secure': os.environ.get('SECURE', '') != 'False'
}


MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD','')
DEFAULT_FROM_EMAIL=os.environ.get('DEFAULT_FROM_EMAIL','')
EMAIL_HOST=os.environ.get('EMAIL_HOST','')
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False