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
