from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

SECRET_KEY = 'as54ty-aseecure-+x6o7ox&1aajtai#_kk(j1)tn45-vxt!rrdghy5(9y3yo7fl5s'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
