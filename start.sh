#!/bin/sh

python manage.py migrate --settings=SardAppren_API.settings.docker

export DJANGO_SETTINGS_MODULE=SardAppren_API.settings.docker
exec gunicorn -b 0.0.0.0:8080 SardAppren_API.wsgi
