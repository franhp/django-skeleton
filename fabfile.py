"""
Management commands

"""
import os

from fabric.api import abort, env, local, settings, task
from fabric.contrib.console import confirm


# Globals
HEROKU_CONFIGS = (
    'DJANGO_SETTINGS_MODULE={{ project_name }}.settings.prod',
    'SECRET_KEY={{ secret_key }}',
)


@task
def gunicorn():
    local("DJANGO_SETTINGS_MODULE='project_name.settings.dev'")
    local("gunicorn -c gunicorn.ini wsgi:application")


@task
def runserver():
    local("DJANGO_SETTINGS_MODULE='project_name.settings.dev'")
    local("python manage.py runserver 0.0.0.0:8000")


@task
def syncdb():
    local('python manage.py syncdb --settings=project_name.settings.dev')


@task
def secure():
    local('python manage.py checksecure')
