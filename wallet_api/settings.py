# Django settings placeholder
from pathlib import Path

import os
BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = 'core.User'
ROOT_URLCONF = 'wallet_api.urls'
#ROOT_URLCONF = 'urls_test'
SECRET_KEY = '4j@(fxmwdbq9qxhwd_7%k4w28%p@b%0q5c-b35%4xyb6j$h2c-'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = True
ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = [
    'wallet_api.authentication.EmailBackend',  # Seu backend por email
    'django.contrib.auth.backends.ModelBackend',  # Fallback padrão (username)
]



INSTALLED_APPS = [
    'django.contrib.admin',  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'rest_framework_simplejwt',
    'wallet_api',
    'wallet',
    'django_extensions',
    'drf_spectacular',
    'drf_yasg',
    # Outros apps...
]

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
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # <- ADICIONADO
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # <- ADICIONADO
    'django.contrib.messages.middleware.MessageMiddleware',  # <- ADICIONADO
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'  # Diretório onde os arquivos estáticos serão servidos

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'desafio_backend',   # Nome que você deu no pgAdmin
        'USER': 'postgres',           # Ou outro, se você criou um diferente
        'PASSWORD': '714705',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}  # <-- Fechar dicionário DATABASES aqui

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Protege toda API por padrão
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}




