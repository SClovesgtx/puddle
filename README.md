
# Introduction

Read about [Model View Template](https://www.geeksforgeeks.org/django-project-mvt-structure/),
and also about [DLT](https://docs.djangoproject.com/en/4.1/ref/templates/language/).

[Here](https://www.youtube.com/watch?v=ao8pCrRqKOs) a easy video overview.

# Commands

Start a new project

```bash
~$  django-admin startproject <project name>
```
Run the server:

```bash
~$  python <project name>/manage.py runserver 
```


Start new app:

```bash 
~$ python manage.py startapp <app name>
```

To register new change in database:

```bash 
~$ python manage.py makemigrations
```

For Django execute theses migrations scripts generated in ```migrations/``` folders, run: 

```bash 
~$ python manage.py migrate
```

To create a user to access admin:

```bash 
~$ python manage.py createsuperuser
```

Now you are able to login as admin at ```localhost/admin/```.