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