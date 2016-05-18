python codango/manage.py makemigrations
python codango/manage.py makemigrations userprofile
python codango/manage.py makemigrations account
python codango/manage.py migrate
gunicorn codango.wsgi --pythonpath=codango --log-file=-