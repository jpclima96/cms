"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cx!j1+m*n87=*iq%m8!^$d8tf0%%=muz4lb5bf4p7h8=zpgfe)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    # Django Filer - optional, but used in most projects
    'filer',
    'easy_thumbnails',
    
    # some content plugins - optional, but used in most projects
    'djangocms_picture',
    'djangocms_text_ckeditor',

    'mob',
    'tailwind',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
                
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# CMS Templates
# https://docs.django-cms.org/en/latest/how_to/install.html#templates

CMS_TEMPLATES = [
    ('mob/home.html', 'Home'),
    ('mob/modelo1.html', 'Modelo 1'),
    ('mob/modelo-static.html', 'Modelo Estático'),
]


# Placeholder
# https://docs.django-cms.org/en/latest/reference/configuration.html#std-setting-CMS_PLACEHOLDER_CONF
CMS_PLACEHOLDER_CONF = {
    'content': {
        'plugins': ['BlockPlugin', 'GridBlockPlugin'],
        'name': "Conteúdo"
        # 'language_fallback': True,
        # 'default_plugins': [
        #     {
        #         'plugin_type': 'TextPlugin',
        #         'values': {
        #             'body':'<p>Lorem ipsum dolor sit amet...</p>',
        #         },
        #     },
        # ],
        # 'child_classes': {
        #     'TextPlugin': ['PicturePlugin', 'LinkPlugin'],
        # },
        # 'parent_classes': {
        #     'LinkPlugin': ['TextPlugin'],
        # },
    },
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LANGUAGES = [
    ('pt-br', 'Português'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# only required for local file storage and serving, in development
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'data/media/'


# Thumbnails
# https://easy-thumbnails.readthedocs.io/en/latest/

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# Picture
# https://github.com/django-cms/djangocms-picture

DJANGOCMS_PICTURE_ALIGN = [
    # Change prefix classes alignment for not use space
    (' object-left', 'Esquerda'),
    (' mx-auto', 'Centro'),
    (' object-right', 'Direita'),
]


# CKEditor
# https://github.com/django-cms/djangocms-text-ckeditor#configuration

TEXT_INLINE_EDITING = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sites
# https://docs.djangoproject.com/en/4.2/ref/contrib/sites/

SITE_ID = 1