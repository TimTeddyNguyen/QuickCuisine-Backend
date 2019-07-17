from base import *

debug = True
DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'quickcuisine',
           'HOST': 'localhost',
           'USER': 'postgres'
    }}