#!/bin/bash
source /var/www/myshop/env/bin/activate
exec gunicorn -c "/var/www/myshop/online_store/gunicorn_config.py" online_store.wsgi
