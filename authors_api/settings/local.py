from .base import *
from .base import env


DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", 'django-insecure-(&=kmj&3bxzx3*-iaqyg8vei16a+t^08g3l1^mod-mu5re7*ds', )

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
