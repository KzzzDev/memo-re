#!/bin/bash

cd app
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py makemigrations memore
python manage.py migrate
python manage.py collectstatic --noinput

# superuser生成
python manage.py custom_createsuperuser --email $DJANGO_ADMIN_EMAIL --password $DJANGO_ADMIN_PASSWORD --username adminname
# APIドキュメント生成
python manage.py spectacular --file schema.yml
# サムネ画像が自動で生成されないため
# python manage.py generateimages
# ER図生成（linux環境をdockerに入れていないのでできなかった）
# python manage.py graph_models -a -o er.png

# configアプリuWSGIに接続。「--py-autoreload 1」でファイル等に変更があった際は自動リロード
uwsgi --socket :8001 \
      --module config.wsgi \
      --py-autoreload 1 \
      --logto /var/log/uwsgi.log \
      --env DJANGO_SETTINGS_MODULE=config.settings.local
