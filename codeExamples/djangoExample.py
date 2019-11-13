## Reference: https://docs.djangoproject.com/en/2.2/intro/tutorial01/

# Installation:
# pip install django

# django-admin startproject ynetHeadlines
# Output:
# ynetHeadlines/
#     manage.py - A command-line utility that lets you interact with this Django project in various ways
#     ynetHeadlines/ - the actual Python package for your project
#         __init__.py
#         settings.py - configuration for this Django project
#         urls.py - The URL declarations for this Django project
#         wsgi.py - An entry-point for WSGI-compatible web servers to serve your project


# python manage.py runserver

## Now let's create an app
# What’s the difference between a project and an app?
# An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

# python manage.py startapp headlines
# Output:
# headlines/
#     __init__.py
#     admin.py
#     apps.py
#     migrations/
#         __init__.py
#     models.py
#     tests.py
#     views.py

# Write your first view: headlines/views.py
# Create headlines/urls.py file

# Add it to the main urls.py file

# GO to: http://localhost:9000/headlines/ in the browser
