#!/bin/sh
# シェル実行が失敗したら終了してエラー出力
set -e -o pipefail

# 実行ディレクトリ取得
ROOT_DIR=$(cd $(dirname $0)/..;pwd)
echo $ROOT_DIR

# "新規アプリ作成"
# 新規ディレクトリ＆アプリ作成
mkdir $ROOT_DIR/app/${1}
django-admin startapp ${1} $ROOT_DIR/app/${1}

# INSTALLED_APPSに新規アプリを追加
sed -i -e "s/'rest_framework',/'rest_framework', \n    '${1}', /" ${ROOT_DIR}/app/config/settings.py

# websiteルーティング追加
sed -i -e "s/\]/    path('${1}\/', include('${1}.urls')),\n\]/" ${ROOT_DIR}/app/config/urls.py


# APP_NAME/urls.py作成
cat > $ROOT_DIR/app/${1}/urls.py << EOF
from django.urls import include, path
# from . import views
from .views import *
app_name = '${1}'

urlpatterns = [
    path('api/jp', JPTestAPI.as_view()),
    path('api/us', USTestAPI.as_view()),
    path('api/br', BRTestAPI.as_view()),
    path('', index, name='index'),
]
EOF

# APP_NAME/views.py修正
cat > $ROOT_DIR/app/${1}/views.py << "EOF"
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
# from django.db.models import Q
import pytz
from datetime import datetime

# REST API 通信テスト用
class JPTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        # return Response(data={'status': dt_now}, status=status.HTTP_200_OK)
        jp = pytz.timezone('Asia/Tokyo')
        return JsonResponse(data={'status': datetime.now(tz=jp)}, status=status.HTTP_200_OK)

class USTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        us = pytz.timezone('US/Eastern')
        return JsonResponse(data={'status': datetime.now(tz=us)}, status=status.HTTP_200_OK)

class BRTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        br = pytz.timezone('Brazil/East')
        return JsonResponse(data={'status': datetime.now(tz=br)}, status=status.HTTP_200_OK)

def index(request):
    return render(request, 'index.html'
EOF

# "テンプレート作成"
# templates＆staticフォルダ階層作成
mkdir $ROOT_DIR/app/templates/${1}

# "「config/urls.py」にルーティングを追加"
sed -i -e "s/]/    path('${1}', include('${1}.urls')),\n]/" $ROOT_DIR/config/urls.py

#*********************************************************
echo "----- django-appstart.sh finish -----"
#*********************************************************