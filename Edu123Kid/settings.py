#coding=utf-8
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iw06g3zbjko)_0h&d&byv%=&h7cf58x-x+%gc1k82w!0xp+ksm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'120.77.35.153',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'writings.apps.WritingsConfig',
    'profiles.apps.ProfilesConfig',
    'home.apps.HomeConfig',
                  
    # 第三方插件
    # ...
    # ...
    'debug_toolbar.apps.DebugToolbarConfig',
    'captcha',
    'aliyunsdkdysmsapi',
    'aliyunsdkcore',
    'vaptchasdk',
    #'djcelery',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
DEBUG_TOOLBAR_CONFIG = {  'JQUERY_URL' : r"http://code.jquery.com/jquery-2.1.1.min.js"}
INTERNAL_IPS = ('127.0.0.1','0.0.0.0',)
DEBUG_TOOLBAR_PANELS = [
                        'debug_toolbar.panels.versions.VersionsPanel',
                        'debug_toolbar.panels.timer.TimerPanel',
                        'debug_toolbar.panels.settings.SettingsPanel',
                        'debug_toolbar.panels.headers.HeadersPanel',
                        'debug_toolbar.panels.request.RequestPanel',
                        'debug_toolbar.panels.sql.SQLPanel',
                        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
                        'debug_toolbar.panels.templates.TemplatesPanel',
                        'debug_toolbar.panels.cache.CachePanel',
                        'debug_toolbar.panels.signals.SignalsPanel',
                        'debug_toolbar.panels.logging.LoggingPanel',
                        'debug_toolbar.panels.redirects.RedirectsPanel',
                        ]


ROOT_URLCONF = 'Edu123Kid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Edu123Kid.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'kid123',
    'USER':'root',
    'PASSWORD':'12808891',
    'HOST':'',
    'PORT':'3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Harbin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')

STATICFILES_DIRS =(os.path.join(BASE_DIR, 'common_static'),)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

LOGIN_URL = '/profiles/login/'

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

###配置Broker
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'

#import djcelery
#djcelery.setup_loader()
