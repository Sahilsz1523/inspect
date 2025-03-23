import os
import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y3jg%-+l#@5ib6*84d@)1831ax%&)!%*cn976m!19k-k!pj^@='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',  # Allow all hosts for simplicity (update this for production)
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myinspect',  # Your app
    'rest_framework',  # Django REST framework
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'myapp.wsgi.application'

# Database Configuration
if os.getenv('DJANGO_ENV') == 'production':
    # Production: Use Railway MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME', 'railway'),  # Railway database name
            'USER': os.getenv('DB_USER', 'root'),  # Railway username
            'PASSWORD': os.getenv('DB_PASSWORD', 'xNCDNIXVvuqqRbaEtLHNEXgyJQOpsKgh'),  # Railway password
            'HOST': os.getenv('DB_HOST', 'monorail.proxy.rlwy.net'),  # Railway host
            'PORT': os.getenv('DB_PORT', '3307'),  # Railway port
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    # Local Development: Use MySQL Workbench
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'myinspect',  # Local database name
            'USER': 'root',  # Local MySQL username
            'PASSWORD': '2005',  # Local MySQL password
            'HOST': 'localhost',  # Local MySQL host
            'PORT': '3307',  # Local MySQL port
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static and Media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myinspect', 'static')]  # For development

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sahilsn2005@gmail.com'  # Your email
EMAIL_HOST_PASSWORD = 'brha djpa hcst vite'  # Your email password

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'