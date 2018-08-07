import os


# prod settings
SECRET_KEY = 'DIFFERENT-IN-PRODUCTION'
DEBUG = False
ALLOWED_HOSTS = ['.aswwu.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'default',
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    },
    'elections': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elections',
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    },
    'jobs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobs',
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    },
    'pages': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pages',
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    },
    'people': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'people',
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    },
}
