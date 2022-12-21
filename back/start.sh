#!/bin/bash

cd app
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py makemigrations memore
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py custom_createsuperuser --email admin@example.com --password admin --userid adminid --username adminname
python manage.py spectacular --file schema.yml

# configアプリuWSGIに接続。「--py-autoreload 1」でファイル等に変更があった際は自動リロード
uwsgi --socket :8001 \
      --module config.wsgi \
      --py-autoreload 1 \
      --logto /var/log/uwsgi.log \
      --env DJANGO_SETTINGS_MODULE=config.settings.local
