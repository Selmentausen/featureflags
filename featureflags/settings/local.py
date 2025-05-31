import os

from celery.schedules import crontab

from .base import *  # noqa: F401,F403

# ruff: noqa: F405

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "local_insecure_password")
DEBUG = True

ALLOWED_HOSTS = []

DATABASES["default"] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.getenv("POSTGRES_DB", "featureflags"),
    "USER": os.getenv("POSTGRES_USER", "ff"),
    "PASSWORD": os.getenv("POSTGRES_PASSWORD", "ffpass"),
    "HOST": os.getenv("POSTGRES_HOST", "db"),
    "PORT": os.getenv("POSTGRES_PORT", "5432"),
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/0"),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

INSTALLED_APPS += ["django_extensions", "debug_toolbar"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]

# Celery
CELERY_BEAT_SCHEDULE = {
    "daily-evaluation-aggregate": {
        "task": "core.tasks.aggregate_flag_evaluations",
        "schedule": crontab(minute=0, hour=0),
    }
}
