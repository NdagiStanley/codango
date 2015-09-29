# codango
Codango is a resource Sharing Social Network for Coders

#Installation
1. Clone the repository into a Virtual Environment. Run `virtualenv <virtualenvname>` to create the virtual environment.
2. Install all the necessary requirements by running `pip install -r requirements.txt` within the virtual environment.
3. Configure your database setting in _codango/settings.py_.
4. Run `python manage.py migrate` to create the user tables and everything required to run the application.
5. Run `python manage.py runserver` to run the app.


## codango apps
1. **account**
2. **resources**

## account
The account app includes all registration and authentication code, it enables you to become a codango user, login, retrieve forgotten password and navigate through your codango account successfully.

## resources
The resources app handles all user resource creation which includes PDF-resources, Code-snippets, Image-resources, Video-resources and link-resources.

## requirements
The following are the installed requirements for codango
- coverage==3.7.1
- dj-database-url==0.3.0
- Django==1.8.3
- django-bootstrap-form==3.2
- django-postgrespool==0.3.0
- funcsigs==0.4
- gunicorn==19.3.0
- hashids==1.1.0
- mock==1.3.0
- pbr==1.5.0
- psycopg2==2.6.1
- requests==2.7.0
- selenium==2.47.1
- six==1.9.0
- SQLAlchemy==1.0.8
- wheel==0.24.0
- whitenoise==2.0.3

## running tests
1. Activate virtual environment.
2. Navigate into the project directory.
3. Run `python manage.py test` to test codango.
4. Run `python manage.py test <appname>` to test an individual app.
5. Run `coverage run manage.py test` to run coverage for codango. 

## authors
[Chidiebere Nnadi](https://github.com/andela-cnnadi)
[Olufunmilade Oshodi](https://github.com/andela-ooshodi)
[Issa Jubril](https://github.com/andela-ijubril)
[Inioluwa Fageyinbo](https://github.com/andela-ifageyinbo)

## copyright
Andela © 2015 CODANGO