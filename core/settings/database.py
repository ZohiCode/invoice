from .base import BASE_DIR
import os
import time

DB_DEBUG = os.environ.get("DB_DEBUG", "false").lower() == "true"


if DB_DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_NAME", "mysql"),
            "USER": os.environ.get("DB_USER", "mysql"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "mysql"),
            "HOST": os.environ.get("DB_HOST", "mysql"),
            "PORT": 3306,
        }
    }
