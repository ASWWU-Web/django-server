SECRET_KEY = 'dev'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'default',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    },
    'elections': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elections',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    },
    'jobs': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobs',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    },
    'pages': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pages',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    },
    'people': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'people',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '8889',
    },
}
