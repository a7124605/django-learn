This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
.gitignore
.python-version
blog/admin.py
blog/apps.py
blog/migrations/0001_initial.py
blog/models.py
blog/static/blog/main.css
blog/templates/blog/about.html
blog/templates/blog/base.html
blog/templates/blog/home.html
blog/tests.py
blog/urls.py
blog/views.py
django_project/asgi.py
django_project/settings.py
django_project/urls.py
django_project/wsgi.py
manage.py
pyproject.toml
users/admin.py
users/apps.py
users/forms.py
users/models.py
users/repomix-output.md
users/templates/users/login.html
users/templates/users/logout.html
users/templates/users/profile.html
users/templates/users/register.html
users/tests.py
users/views.py
```

# Files

## File: users/templates/users/login.html
````html
{% extends "blog/base.html" %} {%load crispy_forms_tags%}{%block content%}
<div class="content-section">
    <form method="POST">
        {%csrf_token%}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Log In</legend>
            {{form|crispy}}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-infof" type="submit">Login</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted"
            >Need An Account?
            <a class="ml-2" href="{%url 'register'%}">Sign UP Now</a>
        </small>
    </div>
</div>
{%endblock content%}
````

## File: users/templates/users/logout.html
````html
{% extends "blog/base.html" %} {%block content%}
<h2>You have been logout</h2>
<div class="border-top pt-3">
    <small class="text-muted">
        <a class="ml-2" href="{%url 'login'%}">Log In Again</a>
    </small>
</div>

{%endblock content%}
````

## File: users/templates/users/profile.html
````html
{% extends "blog/base.html" %} {%load crispy_forms_tags%}{%block content%}
<h1>{{user.username}}</h1>
{%endblock content%}
````

## File: .gitignore
````
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
# Created by https://www.toptal.com/developers/gitignore/api/django,python,visualstudiocode
# Edit at https://www.toptal.com/developers/gitignore?templates=django,python,visualstudiocode

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media

# If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/
# in your Git repository. Update and uncomment the following line accordingly.
# <django-project-name>/staticfiles/

### Django.Python Stack ###
# Byte-compiled / optimized / DLL files
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo

# Django stuff:

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### Python ###
# Byte-compiled / optimized / DLL files

# C extensions

# Distribution / packaging

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.

# Installer logs

# Unit test / coverage reports

# Translations

# Django stuff:

# Flask stuff:

# Scrapy stuff:

# Sphinx documentation

# PyBuilder

# Jupyter Notebook

# IPython

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm

# Celery stuff

# SageMath parsed files

# Environments

# Spyder project settings

# Rope project settings

# mkdocs documentation

# mypy

# Pyre type checker

# pytype static type analyzer

# Cython debug symbols

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

### VisualStudioCode Patch ###
# Ignore all local history of files
.history
.ionide

# End of https://www.toptal.com/developers/gitignore/api/django,python,visualstudiocode
````

## File: .python-version
````
3.13
````

## File: blog/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: blog/apps.py
````python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
````

## File: blog/migrations/0001_initial.py
````python
# Generated by Django 5.2.1 on 2025-05-12 14:08

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
````

## File: blog/static/blog/main.css
````css
body {
    background: #fafafa;
    color: #333333;
    margin-top: 5rem;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #444444;
}

ul {
    margin: 0;
}

.bg-steel {
    background-color: #5f788a;
}

.site-header .navbar-nav .nav-link {
    color: #cbd5db;
}

.site-header .navbar-nav .nav-link:hover {
    color: #ffffff;
}

.site-header .navbar-nav .nav-link.active {
    font-weight: 500;
}

.content-section {
    background: #ffffff;
    padding: 10px 20px;
    border: 1px solid #dddddd;
    border-radius: 3px;
    margin-bottom: 20px;
}

.article-title {
    color: #444444;
}

a.article-title:hover {
    color: #428bca;
    text-decoration: none;
}

.article-content {
    white-space: pre-line;
}

.article-img {
    height: 65px;
    width: 65px;
    margin-right: 16px;
}

.article-metadata {
    padding-bottom: 1px;
    margin-bottom: 4px;
    border-bottom: 1px solid #e3e3e3;
}

.article-metadata a:hover {
    color: #333;
    text-decoration: none;
}

.article-svg {
    width: 25px;
    height: 25px;
    vertical-align: middle;
}

.account-img {
    height: 125px;
    width: 125px;
    margin-right: 20px;
    margin-bottom: 16px;
}

.account-heading {
    font-size: 2.5rem;
}
````

## File: blog/templates/blog/about.html
````html
{% extends "blog/base.html" %} {%block content%}
<h1>About Page</h1>
{%endblock content%}
````

## File: blog/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: django_project/asgi.py
````python
"""
ASGI config for django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_asgi_application()
````

## File: django_project/wsgi.py
````python
"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()
````

## File: manage.py
````python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
````

## File: users/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: users/apps.py
````python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
````

## File: users/forms.py
````python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
````

## File: users/models.py
````python
from django.db import models

# Create your models here.
````

## File: users/repomix-output.md
````markdown
This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
admin.py
apps.py
forms.py
models.py
templates/users/register.html
tests.py
views.py
```

# Files

## File: admin.py
```python
from django.contrib import admin

# Register your models here.
```

## File: apps.py
```python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
```

## File: forms.py
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
```

## File: models.py
```python
from django.db import models

# Create your models here.
```

## File: templates/users/register.html
```html
{% extends "blog/base.html" %} {%load crispy_forms_tags%}{%block content%}
<div class="content-section">
    <form method="POST">
        {%csrf_token%}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Join Today</legend>
            {{form|crispy}}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-infof" type="submit">Sign Up</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted"
            >Already Have An Account?
            <a class="ml-2" href="#">Sign In</a>
        </small>
    </div>
</div>
{%endblock content%}
```

## File: tests.py
```python
from django.test import TestCase

# Create your tests here.
```

## File: views.py
```python
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username} !")
            return redirect("blog_home_page")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
```
````

## File: users/templates/users/register.html
````html
{% extends "blog/base.html" %} {%load crispy_forms_tags%}{%block content%}
<div class="content-section">
    <form method="POST">
        {%csrf_token%}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Join Today</legend>
            {{form|crispy}}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-infof" type="submit">Sign Up</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted"
            >Already Have An Account?
            <a class="ml-2" href="{%url 'login'%}">Sign In</a>
        </small>
    </div>
</div>
{%endblock content%}
````

## File: users/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: users/views.py
````python
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to login!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
````

## File: blog/models.py
````python
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
````

## File: blog/templates/blog/base.html
````html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <!-- Bootstrap CSS -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
            crossorigin="anonymous"
        />

        <link rel="stylesheet" type="text/css" href="{%static 'blog/main.css'%}">

        <title>Django Blog</title>
    </head>
    <body>
        <header class="site-header">
            <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
                <div class="container">
                    <a class="navbar-brand mr-4" href="/">Django Blog</a>
                    <button
                        class="navbar-toggler"
                        type="button"
                        data-toggle="collapse"
                        data-target="#navbarToggle"
                        aria-controls="navbarToggle"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarToggle">
                        <div class="navbar-nav mr-auto">
                            <a class="nav-item nav-link" href="/">Home</a>
                            <a class="nav-item nav-link" href="/about">About</a>
                        </div>
                        <!-- Navbar Right Side -->
                        <div class="navbar-nav ms-auto">
                          {%if user.is_authenticated %}
                          <a class="nav-item nav-link" href="{%url 'profile' %}">Profile</a>
                          <form action="{% url 'logout' %}" method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-outline-light">Logout</button>
                        </form>
                          {%else%}
                            <a class="nav-item nav-link" href="{%url 'login'%}">Login</a>
                            <a class="nav-item nav-link" href="{%url 'register'%}">Register</a>
                          {%endif%}
                        </div>
                    </div>
                </div>
            </nav>
        </header>

        <main role="main" class="container">
          <div class="row">
            <div class="col-md-8">
              {%if messages %}
              {%for message in messages%}
              <div class="alert-{{message.tags}}">
                {{message}}
              </div>
              {%endfor%}
              {%endif%}
              {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
              <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                  <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                  </ul>
                </p>
              </div>
            </div>
          </div>
        </main>

        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"
        ></script>
    </body>
</html>
````

## File: blog/templates/blog/home.html
````html
{% extends "blog/base.html" %} {%block content%} {%for post in posts%}
<article class="media content-section">
    <div class="media-body">
        <div class="article-metadata">
            <a class="mr-2" href="#">{{ post.author }}</a>
                >{{ post.date_posted}}</small
            <small class="text-muted">{{ post.date_posted}}</small>
        </div>
        <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
        <p class="article-content">{{ post.content }}</p>
    </div>
</article>
{% endfor %} {%endblock content%}
````

## File: blog/urls.py
````python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="blog_home_page"),
    path("about/", views.about_page, name="blog_about_page"),
]
````

## File: blog/views.py
````python
from django.shortcuts import render

from .models import Post

# Create your views here.

posts = [
    {
        "author": "Chris",
        "title": "BookA",
        "content": "Some word here",
        "date_posted": "August 26 2025",
    },
    {
        "author": "Ruby",
        "title": "BookB",
        "content": "Some word here",
        "date_posted": "August 24 2022",
    },
    {
        "author": "Andy",
        "title": "BookC",
        "content": "Some word here",
        "date_posted": "August 13 2024",
    },
    {
        "author": "Yolanda",
        "title": "BookD",
        "content": "Some word here",
        "date_posted": "August 01 2017",
    },
]


def home_page(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about_page(request):
    return render(request, "blog/about.html", {"title": "About"})
````

## File: django_project/settings.py
````python
"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#d)&n&3z)jy_hg^aifuy)*cbez7+43o6ok=r%7!*9i@wb_4ar6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "blog.apps.BlogConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "blog_home_page"

LOGIN_URL = "login"
````

## File: django_project/urls.py
````python
"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("", include("blog.urls")),
]
````

## File: pyproject.toml
````toml
[project]
name = "django-learn"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "crispy-bootstrap5>=2025.4",
    "django>=5.2.1",
    "django-crispy-forms>=2.4",
]
````
