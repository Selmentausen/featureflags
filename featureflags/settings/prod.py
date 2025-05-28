import os

from .base import *  # noqa: F401,F403

# ruff: noqa: F405

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

DATABASES["default"] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ["POSTGRES_DB"],
    "USER": os.environ["POSTGRES_USER"],
    "PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "HOST": os.environ["POSTGRES_HOST"],
    "PORT": os.environ.get("POSTGRES_PORT", "5432"),
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ["REDIS_URL"],
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7
