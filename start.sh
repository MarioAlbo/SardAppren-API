#!/bin/sh

python manage.py migrate --settings=SardAppren.settings.docker

export DJANGO_SETTINGS_MODULE=SardAppren.settings.docker
exec gunicorn -b 0.0.0.0:8080 SardAppren.wsgi
