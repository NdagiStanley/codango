python codango/manage.py makemigrations
python codango/manage.py migrate
gunicorn codango.wsgi --pythonpath=codango --log-file=-

webpack
cd codango
python manage.py collectstatic --noinput
