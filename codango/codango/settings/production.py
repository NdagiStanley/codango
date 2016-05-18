# Production specific settings
from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

BOWER_PATH = '/app/node_modules/bower'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# cloudamqp configurations
BROKER_POOL_LIMIT = 3

BROKER_URL = os.getenv('CLOUDAMQP_URL')
