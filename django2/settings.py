"""
Django settings for django2 project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url

# para usar postgree no Heroku, Pega a configuração padrão para Postgree
DATABASES = {
    'default': dj_database_url.config()
}

from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aj!ir%shqvgx$9^f$tr75a4h^3e928kv6p$b&cir2_#(li)^a_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
    'stdimage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # foi substituido pelo pip install dj_static pip uninstall whitenoise abrir o wsgi.py
    # 'whitenoise.middleware.WhiteNoiseMiddleware', # adicionado para servir staticos foi substiuido, mas pra mim funcionou
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'django2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# O Heroku não trabalha com mysql na versão free
    # instale as duas bibliotecas a seguir
        # pip install dj_database_url psycopg2-binary
        # Depois faça a importação do dj_database_url a baixo do os
            # Driver  de conexão no Heroku
                # psycopg2-binary
            
            # para passar as coneões default
                # dj_database_ur
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django2',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': 3306 
#     }
# }


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

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # usado em desenvolvimento
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # usado em produção

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# LOGOUT_REDIRECT_URL = 'index'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# confuguração de email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# EMAIL_BACKEND =
# ‘django.core.mail.backends.smtp.EmailBackend’
# EMAIL_HOST = ‘smtp.gmail.com’
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = ‘your_account@gmail.com’
# EMAIL_HOST_PASSWORD = ‘your account’s password’

"""
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'no-replay@dominio.com.br
EMAIL_PORT = 587
EMAIL_USER_TSL = True
EMAIL_HOST_PASSWORD  = 'sua senha'

"""


# Criar o .gitignore
# python manage.py collectstatic
# ver versão do python que estamos usando e criar um arquivo  chamado runtime.txt na raiz do projeto com a versão do python
# Depois devemos criar o arquivo Procfile
    # web: gunicorn django2.wsgi --log-file -

# Comando para criar uma aplicação
# heroku create django2-eli --buildpack heroku/python
    # caso ocorra erro na runtime.txt verifique se é suportado
    # https://devcenter.heroku.com/articles/python-support
# comando para publicar
# git push heroku main 
# Agora devemos criar o banco de dados com
    # heroku run python manage.py migrate
     # heroku run python manage.py createsuperuser
