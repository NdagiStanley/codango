web: gunicorn codango.wsgi --pythonpath=codango --log-file=-
worker: python codango/manage.py celery worker -B -l info