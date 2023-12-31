"""
Django settings for DjangoChatServer project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cig_*wq)c-avj!o6x*twvykqqaw(dxwu$frt@9j6bg(x&w1)))'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/rooms/'
LOGIN_URL = '/login/'

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

try:
    load_dotenv(dotenv_path, verbose=True, override=True, encoding = 'utf_8')
except UserWarning:
    raise ImproperlyConfigured('.env file not found. Did you forget to add one?')

# Application definition

INSTALLED_APPS = [
    'channels',
    'daphne',

    # contrib.admin er upr bosano lagbe
    # 'grappelli.dashboard',
    # 'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'rest_framework_simplejwt',

    'chatApp',
    'registerApp',
    'productApp',
]

# tik eitar jonno amra "Login, SignUp, LogOut" eigula CALL dite Parbo Nah FRONTEND chara... POSTMAN diyeo Call dite Parbo Nah
CORS_ALLOWED_ORIGINS = [
    os.getenv('FRONTEND_ALLOWED_URL'), #FrontEnd er URL eikane dibo jaate kore FrontEnd CORS bypass korte pare
]

JWT_SECRET_KEY = "Sergio Ramos"
os.getenv('JWT_SECRET_KEY')
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),  # Set the expiration time to 1 hour.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    "ALGORITHM": "HS256",
    "SIGNING_KEY": JWT_SECRET_KEY,
}

# GRAPPELLI configs
GRAPPELLI_ADMIN_TITLE = 'DjangoChat Admin'
GRAPPELLI_INDEX_DASHBOARD = 'DjangoChatServer.dashboard.CustomIndexDashboard'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # for CORS request we need this Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoChatServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoChatServer.wsgi.application'
# Configure the ASGI application
ASGI_APPLICATION = 'DjangoChatServer.asgi.application'

CHANNEL_LAYERS = {
    'default':{
        'BACKEND':'channels.layers.InMemoryChannelLayer'
    }
}


STATICFILES_DIRS = [
    os.path.join(os.path.dirname(__file__), 'static'),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# https://docs.djangoproject.com/en/4.2/topics/i18n/
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = False
DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = "/media/"
STATIC_ROOT = "dist/static/"
MEDIA_ROOT = os.path.join(BASE_DIR , 'other_files/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'