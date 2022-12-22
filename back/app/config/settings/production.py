from .base import *

#####################
# Security settings #
#####################

DEBUG = False

SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

################
# Static files #
################

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DB_NAME'),
        'USER': env('MYSQL_USER_NAME'),
        'PASSWORD': env('MYSQL_USER_PASSWORD'),
        'HOST': env('MYSQL_HOST_PRODUCTION'),
        'PORT': env('MYSQL_PORT'),
    }
}
DATABASES['default']['TIME_ZONE'] = 'Asia/Tokyo'
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['sql_mode'] = 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO'
# DATABASES['default']['init_command'] = 'STRICT_TRANS_TABLES'

##################
# REST Framework #
##################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # Browsable APIの非表示
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}


###########
# Logging #
###########

LOGGING = {
    # スキーマバージョンは「1」固定
    'version': 1,
    # すでに作成されているロガーを無効化しないための設定
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 本番用
        'production': {
            'format': '{asctime} <{process:d},{thread:d}> [{levelname}] '
                      '{pathname}:{lineno:d} {message}',
            'style': '{',
        },
    },
    # ハンドラ
    'handlers': {
        # ファイル出力用ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{BASE_DIR.name}/app.log',
            'formatter': 'production',
        },
    },
    # ルートロガー
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
    # その他のロガー
    'loggers': {
        # Django本体が出力するログ全般を扱うロガー
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
