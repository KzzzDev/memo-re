from .base import *

#####################
# Security settings #
#####################

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

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
        'NAME': env.get_value('MYSQL_DB_NAME'),
        'USER': env.get_value('MYSQL_USER_NAME'),
        'PASSWORD': env.get_value('MYSQL_PASSWORD'),
        'HOST': env.get_value('MYSQL_HOST_PRODUCTION'),
        'PORT': env.get_value('MYSQL_PORT'),
    }
}
DATABASES['default']['TIME_ZONE'] = 'Asia/Tokyo'
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['sql_mode'] = 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO'
# DATABASES['default']['init_command'] = 'STRICT_TRANS_TABLES'

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

###################
# Stripe settings #
###################

# Stripe 公開可能キー
# STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
# Stripe シークレットキー
# STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
