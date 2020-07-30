import os
import datetime
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from datetime import timedelta
# import dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8boax9dercf7r8hfio78yez768j@5+z2x^9)hh!o18__8kt$ft'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# PUT THESE IN THE DOTENV FILE
# AUTH0 Django Application Settings
# AUTH0_CLIENT_ID = "7ECrruuGVEjBOGcGyTqbRPvg4hQFXqRa"

# Quantum-Capstone-API clientID
AUTH0_CLIENT_ID = "kaXZdymNjopdmrlQpOL5mMBQZyvrSry0"


# MANAGEMENT-API - client-id
# AUTH0_CLIENT_ID = '5e711bac91a8780913c58961'


AUTH0_DOMAIN = "dev-405n1e6w.auth0.com"

# MANAGEMENT API SECRET
# AUTH0_CLIENT_SECRET = "yJj0SzZCHm5s9WeAOCPOyjMjW9Rg9x7wtb6qqTMeqq7mcOpuN91vnbZ1lqKJ-fJS"


# QUANTUMAPI SECRET
AUTH0_CLIENT_SECRET = 'krWJ-Lb5wYIVJtXvNSluSbj6dLTYW1hODutzoeAlZl9Km2rAtMM9QhN_sWLzIQ33'
# grant_type":"client_credentials"

API_IDENTIFIER = 'https://api.quantumcoasters.com'


# API_IDENTIFIER = 'https://dev-405n1e6w.auth0.com/api/v2/'
# PUBLIC_KEY = None
# JWT_ISSUER = None

# AUTH0 Django APPLICATION SETTINGS
# SOCIAL_AUTH_TRAILING_SLASH = False
# SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-405n1e6w.auth0.com'
# SOCIAL_AUTH_AUTH0_KEY = '7ECrruuGVEjBOGcGyTqbRPvg4hQFXqRa'
# SOCIAL_AUTH_AUTH0_SECRET = 'yJj0SzZCHm5s9WeAOCPOyjMjW9Rg9x7wtb6qqTMeqq7mcOpuN91vnbZ1lqKJ-fJS'
# SOCIAL_AUTH_AUTH0_SCOPE = [
#     'openid',
#     'profile',
#     'email'
# ]


# THEN LOAD THE ENV VARIABLES LIKE BELOW:
# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)

# AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
# API_IDENTIFIER = os.environ.get('API_IDENTIFIER')
# PUBLIC_KEY = None
# JWT_ISSUER = None



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'corsheaders',
    'quantumapi',
    'rest_framework_jwt',
    'social_django',
    'django_filters',
]
    # 'drf_queryfields',



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# REST_USE_JWT = True



# USER_SETTINGS = getattr(settings, 'SIMPLE_JWT', None)

# Custom User Model - models.User/ views.UserViewset
AUTH_USER_MODEL = 'quantumapi.User'

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/home'


# if AUTH0_DOMAIN:
#     JWT_ISSUER = 'https://' + AUTH0_DOMAIN + '/'

# apiexample/settings.py

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'quantumapi.utils.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'quantumapi.utils.jwt_decode_token',
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': API_IDENTIFIER,
    'JWT_ISSUER': 'https://dev-405n1e6w.auth0.com/',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}


AUTHENTICATION_BACKENDS = {
    # FOR DJANGO WEB APP BACKEND
    # 'quantumapi.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
}


ROOT_URLCONF = 'quantumapp.urls'


CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
)


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

WSGI_APPLICATION = 'quantumapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Django All-Auth Settings
# https://django-allauth.readthedocs.io/en/latest/configuration.html

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'None'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'None'

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
REST_AUTH_SERIALIZERS = { 'USER_DETAILS_SERIALIZER':'quantumapi.views.UserSerializer' }
# FIXTURE_DIRS = ('/Users/matthewcrook/code/nss/frontEnd/quantumapp/quantumapi/fixtures', )



# CLOUDINARY_URL = "cloudinary://418576712586226:IaXis96Iz93J6NH7PTrU1clKpGM@capstone-project"


# cloudinary.config(
#     cloud_name="capstone-project",
#     api_key="418576712586226",
#     api_secret="IaXis96Iz93J6NH7PTrU1clKpGM"
# )

# Custom Serializers for UserProfile to override Django User model
# REST_AUTH_SERIALIZERS = { 'USER_DETAILS_SERIALIZER':'users.serializers.UserProfileSerializer' }
# AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# Custom User to Override and tie Django user to UserProfile
# AUTHENTICATION_BACKENDS = (
#     'myproject.auth_backends.UserProfileModelBackend',
# )


# DJANGO SIMPLEJWT SETTINGS
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,

#     'ALGORITHM': 'RS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }


# DJANGO REST JWT SETTINGS
# JWT_AUTH = {
#     'JWT_SECRET_KEY': settings.SECRET_KEY,
#     'JWT_GET_USER_SECRET_KEY': None,
#     'JWT_PRIVATE_KEY': None,
#     'JWT_PUBLIC_KEY': None,
#     'JWT_ALGORITHM': 'HS256',
#     # 'JWT_ALGORITHM': 'RS256',
#     'JWT_AUDIENCE': None,
#     'JWT_ISSUER': None,
#     'JWT_ENCODE_HANDLER':
#         'rest_framework_jwt.utils.jwt_encode_payload',
#     'JWT_DECODE_HANDLER':
#         'rest_framework_jwt.utils.jwt_decode_token',
#     'JWT_PAYLOAD_HANDLER':
#         'rest_framework_jwt.utils.jwt_create_payload',

#     'JWT_PAYLOAD_GET_USERNAME_HANDLER':
#         'rest_framework_jwt.utils.jwt_get_username_from_payload_handler',
#     # 'JWT_PAYLOAD_GET_USERNAME_HANDLER':
#     #     'quantumapi.utils.jwt_get_username_from_payload_handler',

#     'JWT_PAYLOAD_INCLUDE_USER_ID': True,
#     'JWT_VERIFY': True,
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_LEEWAY': 0,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#         'rest_framework_jwt.utils.jwt_create_response_payload',
#     'JWT_AUTH_COOKIE': None,
#     # 'JWT_AUTH_COOKIE': 'quantumapp_token',
#     # 'JWT_AUTH_COOKIE_DOMAIN': 'http://localhost:8000',
#     'JWT_AUTH_COOKIE_DOMAIN': None,
#     'JWT_AUTH_COOKIE_PATH': '/',
#     'JWT_AUTH_COOKIE_SECURE': True,
#     'JWT_AUTH_COOKIE_SAMESITE': 'Lax',
#     'JWT_IMPERSONATION_COOKIE': None,
#     'JWT_DELETE_STALE_BLACKLISTED_TOKENS': False,
# }


# List of settings that may be in string import notation.
# IMPORT_STRINGS = (
#     'JWT_ENCODE_HANDLER',
#     'JWT_DECODE_HANDLER',
#     'JWT_PAYLOAD_HANDLER',
#     'JWT_PAYLOAD_GET_USERNAME_HANDLER',
#     'JWT_RESPONSE_PAYLOAD_HANDLER',
#     'JWT_GET_USER_SECRET_KEY',
# )


# api_settings = APISettings(USER_SETTINGS, SIMPLE_JWT, IMPORT_STRINGS)


# # check if settings have valid values
# if not isinstance(api_settings.JWT_EXPIRATION_DELTA, datetime.timedelta):  # pragma: no cover

#     raise ImproperlyConfigured(
#         '`JWT_EXPIRATION_DELTA` setting must be instance of '
#         '`datetime.timedelta`')

# if not isinstance(
#         api_settings.JWT_REFRESH_EXPIRATION_DELTA, datetime.timedelta):  # pragma: no cover

#     raise ImproperlyConfigured(
#         '`JWT_REFRESH_EXPIRATION_DELTA` setting must be instance of '
#         '`datetime.timedelta`')
