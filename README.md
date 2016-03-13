# django-playground

### Run the site on development webserver

`python manage.py runserver`

### Run python shell

`python manage.py shell`

### Run tests

`python manage.py test polls`

### Create/Update database

`python manage.py migrate`

## Packaging

See [Reusable apps] (https://docs.djangoproject.com/en/1.9/intro/reusable-apps/) for details.

- copy `/polls` outside the project folder to a parent folder `django-polls`
- create `LICENSE`, `MANIFEST`, `README.rst` and `setup.py`
- within `django-polls` run `python setup.py sdist`
- this should generate a *dist* folder with the package `django-polls-0.1.zip`

### Using the package

Prefered way is to install the package in *virtualenv* using *pip* `pip install django-polls-0.1.tar.gz`. Then follow instructions in `README.rst` (add the app `polls` into `INSTALLED_APPS` and setup `URLconf`).

