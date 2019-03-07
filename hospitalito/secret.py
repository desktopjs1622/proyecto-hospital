# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@5#vm+#b1+h57s5joikt5qm(k2*b)n4kik@tfnmavretur$8lx'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'HOST': 'localhost',
        'NAME': 'Hospital',
        'PASSWORD': 'urbina29$',
        'PORT': '5432',
        'USER':'postgres'

    }
}