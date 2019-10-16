# pylint: skip-file

# This setting file is here as a template only, it is currently created on deployment and
# can be used to override development settings for the production environment

# SECURITY WARNING: don't run with debug turned on in production!

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["staging.smartbiogas.io"]

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
