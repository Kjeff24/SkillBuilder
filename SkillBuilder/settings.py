from pathlib import Path
import os
from dotenv import load_dotenv
import sys
from django.utils.translation import gettext_lazy as _
import nltk

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-94wm*9rwwbza_6@qdyvxki!gy0-#2$%&$h7bl*ibx86fy=)$yu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["https://skillbuilder-production.up.railway.app"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'myapp.apps.MyappConfig',
    'course.apps.CourseConfig',
    'quiz.apps.QuizConfig',
    'employerAdmin.apps.EmployeradminConfig',
    'event.apps.EventConfig',
    'chatbot.apps.ChatbotConfig',
    'mcqGenerator.apps.McqgeneratorConfig',
    'django_extensions',
]

AUTH_USER_MODEL  = 'myapp.User'


LOGIN_REDIRECT_URL = '/employer_admin/'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SkillBuilder.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates'
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "SkillBuilder.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = 'images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 600

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# VIDEO STREAMING
APP_ID = os.getenv('APP_ID')
APP_CERTIFICATE = os.getenv('APP_CERTIFICATE')

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

# # Define the NLTK data directory path within your project
# NLTK_DATA_DIR = os.path.join(BASE_DIR, 'corpora')

# # Define the NLTK data directory path within your project
# nltk.data.path.append(NLTK_DATA_DIR)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# Create uml diagram 
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}