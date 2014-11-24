"""
Django settings for spectrewerks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ALLOWED_HOSTS = ['*']

# Application definition

# built in django apps
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# extra apps used in project
THIRD_PARTY_APPS = (

)

# custom built apps (the actual app we are building)
LOCAL_APPS = (
    'reloading_collection',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'spectrewerks.urls'

WSGI_APPLICATION = 'spectrewerks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
#    os.path.join(PROJECT_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'staticfiles'),
    #    os.path.join(BASE_DIR, 'static'),
)

# extra templates
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
#    os.path.join(BASE_DIR, 'reloading/templates'),
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

# try to load local only settings (this will not be pushed to repo!)
try:
    from local_settings import *
except ImportError:
    pass

# try to load production only settings (this will not be pushed to repo!)
try:
    from prod_settings import *
except ImportError:
    pass

