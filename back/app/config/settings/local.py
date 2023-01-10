from .base import *

#####################
# Security settings #
#####################

DEBUG = True

SECRET_KEY = '<fake-secret-key>'

ALLOWED_HOSTS = ['*']

################
# Static files #
################

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DB_NAME'),
        'USER': env('MYSQL_USER_NAME'),
        'PASSWORD': env('MYSQL_USER_PASSWORD'),
        'HOST': env('MYSQL_HOST_LOCAL'),
        'PORT': env('MYSQL_PORT'),
    }
}
DATABASES['default']['TIME_ZONE'] = 'Asia/Tokyo'
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['sql_mode'] = 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO'
# DATABASES['default']['init_command'] = 'STRICT_TRANS_TABLES'

#####################
# Django Extensions #
#####################

INSTALLED_APPS += (
    'django_extensions',
)

###################
# drf-spectacular #
###################

SPECTACULAR_SETTINGS = {
    'TITLE': 'memo:re_API',
    'DESCRIPTION': '未来創造展「memo:re」のAPIドキュメントです。',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

########
# CORS #
########

# クロスオリジン許可
CORS_ORIGIN_ALLOW_ALL = True

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
        # 開発用
        'development': {
            'format': '[{name}] {asctime} [{levelname}] {pathname}:{lineno:d} '
                      '{message}',
            'style': '{',
        },
    },
    # ハンドラ
    'handlers': {
        # コンソール出力用ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'development',
        },
    },
    # ルートロガー
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    # その他のロガー
    'loggers': {
        # 自作アプリケーションごとにロガーを定義することも可能
        'memore': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体が出力するログ全般を扱うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 発行されるSQL文を出力するためのロガー
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}

########################
# Django Debug Toolbar #
########################

if DEBUG:
    def show_toolbar(request):
        return True


    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
