command = '/var/www/myshop/env/bin/gunicorn'
python_path = '/var/www/myshop/online_store'
bind = '127.0.0.1:8001'
workers = 5
user = 'www'
raw_env = 'DJANGO_SETTINGS_MODULE=online_store.settings'
