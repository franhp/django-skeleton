

Install
=======

To create a new  base project, run the following commands:

    $ pip install requirements.txt
    $ django-admin.py startproject --template=https://github.com/rdegges/django-skel/zipball/master woot
    $ heroku config:add DJANGO_SETTINGS_MODULE=myproject.settings.prod
    $ heroku config:add SECRET_KEY=putsomethingfairlycomplexhere
