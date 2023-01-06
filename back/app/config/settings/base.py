import os
import environ
from datetime import timedelta
from pathlib import Path

###############
# Build paths #
###############

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)

###############
# env #
###############

env = environ.Env()
env.read_env('.env')

############
# Security #
############

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

#################
# Core settings #
#################

INSTALLED_APPS = [
    'jazzmin',  # 管理サイトのデザイン
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    # 'django_boost',
    # 'import_export',
    # 'django_tables2',
    'imagekit',  # サムネ生成
    'django_cleanup',  # 画像の自動消去
    'djoser',  # JWT
    'corsheaders',  # CORS
    'rest_framework',
    'drf_spectacular',  # APIドキュメント

    # My applications
    'accounts.apps.AccountsConfig',
    'apiv1.apps.Apiv1Config',
    'memore.apps.MemoreConfig',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

##################
# Authentication #
##################

# AUTH_USER_MODEL = 'accounts.CustomUser'

# LOGIN_REDIRECT_URL = 'account_login'


#######################
# Password validation #
#######################

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

########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

################
# Static files #
################

STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'

##################
# REST Framework #
##################

REST_FRAMEWORK = {
    # デフォルトのアクセス制限
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # 認証にJWTを利用
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # APIドキュメント作成
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    # 認証タイプ
    'AUTH_HEADER_TYPES': ('JWT',),
    # アクセストークン(1時間)
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    # リフレッシュトークン(3日)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    # デフォルトのidを id -> userid に変更
    # 'USER_ID_FIELD': 'userid',
}

DJOSER = {
    # シリアライザの読み込み先
    'SERIALIZERS': {
        'activation': 'djoser.serializers.ActivationSerializer',
        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        'set_username': 'djoser.serializers.SetUsernameSerializer',
        'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
        'username_reset': 'djoser.serializers.SendEmailResetSerializer',
        'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
        'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',
        'user_create': 'djoser.serializers.UserCreateSerializer',
        'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'user': 'djoser.serializers.UserSerializer',
        'current_user': 'djoser.serializers.UserSerializer',
        'token': 'djoser.serializers.TokenSerializer',
        'token_create': 'djoser.serializers.TokenCreateSerializer',
    },
    # メールアドレスでログイン
    # 'LOGIN_FIELD': 'email',
    # # アカウント本登録メール
    # 'SEND_ACTIVATION_EMAIL': True,
    # # アカウント本登録完了メール
    # 'SEND_CONFIRMATION_EMAIL': True,
    # # メールアドレス変更完了メール
    # 'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # # パスワード変更完了メール
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # # アカウント登録時に確認用パスワード必須
    # 'USER_CREATE_PASSWORD_RETYPE': True,
    # # メールアドレス変更時に確認用メールアドレス必須
    # 'SET_USERNAME_RETYPE': True,
    # # パスワード変更時に確認用パスワード必須
    # 'SET_PASSWORD_RETYPE': True,
    # # アカウント本登録用URL
    # 'ACTIVATION_URL': 'activate/{uid}/{token}',
    # # メールアドレスリセット完了用URL
    # 'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    # # パスワードリセット完了用URL
    # 'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    # # カスタムユーザー用シリアライザー
    # 'SERIALIZERS': {
    #     'user_create': 'accounts.serializers.UserSerializer',
    #     'user': 'accounts.serializers.UserSerializer',
    #     'current_user': 'accounts.serializers.UserSerializer',
    # },
    # 'EMAIL': {
    #     # アカウント本登録
    #     'activation': 'accounts.email.ActivationEmail',
    #     # アカウント本登録完了
    #     'confirmation': 'accounts.email.ConfirmationEmail',
    #     # パスワードリセット
    #     'password_reset': 'accounts.email.PasswordResetEmail',
    #     # パスワードリセット完了
    #     'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmationEmail',
    #     # メールアドレスリセット
    #     'username_reset': 'accounts.email.UsernameResetEmail',
    #     # メールアドレスリセット完了
    #     'username_changed_confirmation': 'accounts.email.UsernameChangedConfirmationEmail',
    # },
}

#######################
# Other core settings #
#######################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# メッセージタグの設定
# MESSAGE_TAGS = {
#     messages.ERROR: 'danger',
# }

#######################
# django-allauth #
#######################

# # django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
# SITE_ID = 1
#
# AUTHENTICATION_BACKENDS = (
#     'allauth.account.auth_backends.AuthenticationBackend',  # 一般ユーザー用（メールアドレス認証）
#     'django.contrib.auth.backends.ModelBackend',  # 管理サイト用（ユーザー名認証）
# )
#
# # メールアドレス認証に変更する設定
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USERNAME_REQUIRED = False
#
# # サインアップにメールアドレス確認をはさむよう設定
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_REQUIRED = True
#
# # ログイン／ログアウト後の遷移先設定
# LOGIN_REDIRECT_URL = 'ctf:problem_list'
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
#
# # ログアウトリンクのクリック一発でログアウトする設定
# ACCOUNT_LOGOUT_ON_GET = True
#
# # 送信元メールアドレス
# DEFAULT_FROM_EMAIL = 'beginnersctf@gmail.com'
#
# # コンソールにメールを送信
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# # adapterをオーバーライドするための設定
# ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'

# バックアップパッチ用
# BACKUP_PATH = 'backup/'
# NUM_SAVED_BACKUP = 30

##################
# django-bootstrap5 #
##################

# BOOTSTRAP5 = {
#     'set_placeholder': False,
# }

##################
# django-tables2 #
##################

# DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

###################
# Stripe settings #
###################

# Stripe 公開可能キー
# STRIPE_PUBLISHABLE_KEY = '<stripe-publishable-key>'
# Stripe シークレットキー
# STRIPE_SECRET_KEY = '<stripe-api-secret-key>'
