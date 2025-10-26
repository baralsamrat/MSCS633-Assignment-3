import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "dev-key"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "bot",
]

MIDDLEWARE = []
ROOT_URLCONF = "chatbot_terminal.urls"
TEMPLATES = []
WSGI_APPLICATION = "chatbot_terminal.wsgi.application"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "django.sqlite3"}
}

CHATTERBOT_DB_PATH = str(BASE_DIR / "chatterbot.sqlite3")
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
