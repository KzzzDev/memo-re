#!/bin/sh
# シェル実行が失敗したら終了してエラー出力
set 'echo -e -o pipefail'

# ルートディレクトリ取得
ROOT_DIR=$(cd $(dirname $0)/..;pwd)
echo ${ROOT_DIR}

# 各種モジュールインポートを追記
if ! grep -q "import os" "${ROOT_DIR}/app/config/settings.py" ;then
    sed -i -e "s/from pathlib import Path/from pathlib import Path \nimport os\nimport json\nfrom six.moves.urllib import request\nfrom cryptography.x509 import load_pem_x509_certificate\nfrom cryptography.hazmat.backends import default_backend/" ${ROOT_DIR}/app/config/settings.py
fi

# BASE_DIR変更
sed -i -e "s/BASE_DIR = Path(__file__).resolve().parent.parent/BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))/" ${ROOT_DIR}/app/config/settings.py

# INSTALLED_APPSにrest_frameworkとrest_framework_jwtとcorsheadersを追加
if ! grep -q "'rest_framework'," "${ROOT_DIR}/app/config/settings.py" ;then
    sed -i -e "s/'django.contrib.staticfiles',/'django.contrib.staticfiles',\n    'rest_framework', \n    'rest_framework_jwt', \n    'corsheaders',/" ${ROOT_DIR}/app/config/settings.py
fi

# MIDDLEWAREにcorsheadersミドルウェアを追記
if ! grep -q "'corsheaders.middleware.CorsMiddleware'," "${ROOT_DIR}/app/config/settings.py" ;then
sed -i -e "s/'django.middleware.common.CommonMiddleware',/'corsheaders.middleware.CorsMiddleware', \n    'django.middleware.common.CommonMiddleware', \n/" ${ROOT_DIR}/app/config/settings.py
fi

# テンプレートディレクトリ設定
sed -i -e "s/'DIRS': \[\],/'DIRS': \[os.path.join(BASE_DIR, \"app\/templates\")\],/" ${ROOT_DIR}/app/config/settings.py

# 言語をjaに変更
sed -i -e "s/LANGUAGE_CODE = 'en-us'/LANGUAGE_CODE = 'ja'/" ${ROOT_DIR}/app/config/settings.py

# タイムゾーンをAsia/Tokyoに変更
sed -i -e "s/TIME_ZONE = 'UTC'/TIME_ZONE = 'Asia\/Tokyo'/" ${ROOT_DIR}/app/config/settings.py

# DATEBASEパス変更
sed -i -e "s/'NAME': BASE_DIR \/ 'db.sqlite3',/'NAME': BASE_DIR+'\/app\/db.sqlite3',/" ${ROOT_DIR}/app/config/settings.py

# ALLOWED_HOSTSにlocalhostと127.0.0.1追加
sed -i -e "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\n  '127.0.0.1', \n    'localhost', \]/" ${ROOT_DIR}/app/config/settings.py

# STATIC_ROOT追記
sed -i -e "s/STATIC_URL = '\/static\/'/STATIC_URL = '\/static\/'\nSTATIC_ROOT = os.path.join(BASE_DIR, 'static')/" ${ROOT_DIR}/app/config/settings.py

# REST_FRAMEWORK設定追記
if ! grep -q "REST_FRAMEWORK = {" "${ROOT_DIR}/app/config/settings.py" ;then
echo "# REST_FRAMEWORK設定
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# クロスオリジン許可
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
)
" >> ${ROOT_DIR}/app/config/settings.py
fi

# importにincludeモジュールを追加＆napp_name設定
sed -i -e "s/from django.urls import path/from django.urls import path, include \nfrom rest_framework.documentation import include_docs_urls\n/" ${ROOT_DIR}/app/config/urls.py
# APIドキュメントルート追加
sed -i -e "s/path('admin\/', admin.site.urls),/path('admin\/', admin.site.urls),\n    path('docs\/', include_docs_urls(title='API Document')),\n/" ${ROOT_DIR}/app/urls.py

# templates＆staticフォルダ階層作成
mkdir ${ROOT_DIR}/app/templates
mkdir ${ROOT_DIR}/app/static && mkdir ${ROOT_DIR}/app/static/css ${ROOT_DIR}/app/static/js ${ROOT_DIR}/app/static/images

# base.html作成
cat > ${ROOT_DIR}/app/templates/base.html << "EOF"
<!DOCTYPE html>
{% load tz %}
{% load static %}
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    {% block style %}{% endblock %}
</head>
<body>
    {% if messages %}
    <ul class="pl-0 ml-3">
    {% for message in messages %}
        <li class="alert alert-{{ message.tags }}">{{ message }}<button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">x</span> </button></li>
    {% endfor %}
    </ul>
    {% endif %}
    {% block content %}
    {% endblock %}
    {% block script %}{% endblock %}
</body>
</html>
EOF

# index.html作成
cat > ${ROOT_DIR}/app/templates/index.html << "EOF"
{% extends "base.html" %}
{% load static %}
{% block title %}ページタイトル{% endblock %}
{% block style %}
{% endblock %}
{% block breadcrumb %}
{% endblock %}
{% block content %}
インデックスページのコンテンツを表示中
{% endblock %}
{% block script %}
{% endblock %}
EOF

# template.html作成
cat > ${ROOT_DIR}/app/templates/template.html << EOF
{% extends "base.html" %}
{% load static %}
{% block title %}ページタイトル{% endblock %}
{% block style %}
{% endblock %}
{% block breadcrumb %}
{% endblock %}
{% block content %}
コンテンツテンプレートです
{% endblock %}
{% block script %}
{% endblock %}
EOF

#*********************************************************
echo "----- django-settings.sh finish -----"
#*********************************************************