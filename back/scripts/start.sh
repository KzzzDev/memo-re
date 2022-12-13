#!/bin/bash

cd app
python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic

# configアプリuWSGIに接続。「--py-autoreload 1」でファイル等に変更があった際は自動リロード
uwsgi --socket :8001 --module config.wsgi --py-autoreload 1 --logto /tmp/uwsgi.log

#python manage.py runserver 0.0.0.0:8001