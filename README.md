# Codango

## Description
Codango is a Resource Sharing Social Network for Coders.

Codango resource sharing includes *Code Snippets* posting and *Pdf* uploads. Codango also allows for *Pair Programming* and *Networking* among coders.

## Installation
1. Clone the repository and create a Virtual Environment.
- Run `virtualenv <virtualenvname>` to create the virtual environment or `mkvirtualenv <virtualenvname>` if using virtualenv wrapper to create the virtual environment.
2. Install all the necessary requirements by running `pip install -r requirements.txt` within the virtual environment.
3. Configure your database configurations in a development.py and save in the settings folder
4. Create a .env.yml to hold all your environment variables, like your secret key, save in the same level as your README.md file (sample shown below)
5. Run `bower install` to install all front end dependencies. Please ensure you are on the same level with .bowerrc when you run this command
6. Run `python manage.py collectstatic` to copy all your static files into the staticfiles directory
7. Run `python manage.py makemigrations` and `python manage.py migrate` to create the necessary tables and everything required to run the application.
7. Run `python manage.py runserver` to run the app.
8. Run coverage `coverage run manage.py test` to know how much the app is covered by automated testing.
9. View the report of the coverage on your terminal `coverage report`.
10. Produce the html of coverage result `coverage html`.

## Sample .env.yml format
```
SECRET_KEY:
  "sample_key"
```

## Requirements
The following are the installed requirements for codango
- amqp==1.4.7
- anyjson==0.3.3
- appnope==0.1.0
- billiard==3.3.0.21
- celery==3.1.19
- cloudinary==1.1.3
- coverage==3.7.1
- decorator==4.0.4
- dj-database-url==0.3.0
- Django==1.8.3
- django-all-access==0.7.2
- django-bootstrap-form==3.2
- django-bower==5.0.4
- django-celery==3.1.17
- django-endless-pagination==2.0
- django-envie==0.0.9
- django-postgrespool==0.3.0
- funcsigs==0.4
- gnureadline==6.3.3
- gunicorn==19.3.0
- hashids==1.1.0
- ipdb==0.8.1
- ipython==4.0.0
- ipython-genutils==0.1.0
- kombu==3.0.29
- meld3==1.0.2
- mock==1.3.0
- oauthlib==1.0.3
- path.py==8.1.2
- pbr==1.8.1
- pexpect==4.0.1
- pickleshare==0.5
- Pillow==2.9.0
- psycopg2==2.6.1
- ptyprocess==0.5
- pycrypto==2.6.1
- python-openid==2.2.5
- pytz==2015.7
- PyYAML==3.11
- reportlab==3.2.0
- requests==2.7.0
- requests-oauthlib==0.5.0
- selenium==2.48.0
- sendgrid==1.5.14
- simplegeneric==0.8.1
- six==1.9.0
- smtpapi==0.2.0
- SQLAlchemy==1.0.8
- traitlets==4.0.0
- wheel==0.24.0
- whitenoise==2.0.3

## Running tests
1. Activate virtual environment.
2. Navigate into the project directory.
3. Run `python manage.py test` to test codango.
4. Run `python manage.py test <appname>` to test an individual app.
5. Run `coverage run manage.py test` to run coverage for codango.

## Authors
###### [Joan Ngatia](https://github.com/andela-jngatia)
###### [Stanley Ndagi](https://github.com/andela-sndagi)
###### [Achile Egbunu](https://github.com/andela-aegbunu)

## Copyright
Andela © 2015 CODANGO