#!/bin/bash
set 'echo -e -o pipefail'

unix_today=$(date +'%s')
unix_today=$((unix_today+32400))
jst_ymd_today=$(date '+%Y/%m/%d %H:%M:%S' --date "@$unix_today")

# メインプロジェクトフォルダが無ければセットアップ実行
if [ ! -d /usr/src/app ]; then
# if [ ! -d /code/app ]; then
    echo "----- ${jst_ymd_today} | Project initialization -----"
    mkdir app && cd app && django-admin startproject config .
    sleep 10
    # djangoセットアップ＆サーバー起動
    bash /usr/src/app/scripts/django-settings.sh
    bash /usr/src/app/scripts/django-appstart.sh api
    # python manage.py createsuperuser
    echo "----- ${jst_ymd_today} | Initialization completed -----"
else
    echo "----- ${jst_ymd_today} | container update -----"
fi

cd app
python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic

# 静的ファイルディレクトリをstatic指定ディレクトリに集約コピー(--noinputで対話プロンプトを無視)
python manage.py collectstatic --noinput
# configアプリuWSGIに接続。「--py-autoreload 1」でファイル等に変更があった際は自動リロード
uwsgi --socket :8001 --module config.wsgi --py-autoreload 1 --logto /tmp/uwsgi.log

# python manage.py runserver 0.0.0.0:8001