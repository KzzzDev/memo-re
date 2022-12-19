#!/bin/bash

cd app
python manage.py makemigrations accounts
# python manage.py makemigrations app
python manage.py migrate
python manage.py collectstatic --noinput

# django-debug-toolbar
# staticファイルのロード先を別フォルダに設定しているため、CSSが効かない問題を解決
# https://unisia-se.com/detail/33/
# cp -r /usr/local/lib/python3.9/site-packages/debug_toolbar/static/debug_toolbar /usr/src/app/app/static
# # 管理サイトのCSS
# cp -r /usr/local/lib/python3.9/site-packages/django/contrib/admin/static/admin/ /usr/src/app/app/static

python manage.py custom_createsuperuser --email admin@example.com --password admin

# configアプリuWSGIに接続。「--py-autoreload 1」でファイル等に変更があった際は自動リロード
uwsgi --socket :8001 \
      --module config.wsgi \
      --py-autoreload 1 \
      --logto /var/log/uwsgi.log \
      --env DJANGO_SETTINGS_MODULE=config.settings.local
