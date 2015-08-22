<<<<<<< HEAD
# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.7.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
=======
# PharmaOnline Project

**PharmaOnline** is a project whose main goal is to facilitate access to health related products, especially pharmaceuticals, in Haiti.
Often, it is difficult for people to find their prescribed drugs (*and sometimes even over-the-counter drugs*) around Haiti's cities due to various reasons.

- Scarcity of the drugs itself

- An unorganized system

- Lack of documentation and real time knowledge of the generic drugs that are available or unavailable on the market.


Because of this, we found that a system that tells where and when (eventually) the product is available *could help make healthcare in general an easier area to navigate.*

This project was built with the [Heroku Django Starter template](https://github.com/heroku/heroku-django-template)

Temporary link to project (will be moved): https://webrx.herokuapp.com

>>>>>>> origin/master
