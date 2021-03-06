from .settings import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
import os
DATABASES['default'] =  dj_database_url.config()
SECRET_KEY = os.environ['SECRET_KEY']
print(' heroku database')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
DEBUG = False

#   from original settings
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
# STATIC_ROOT = os.path.join(BASE_DIR, "project_static")
