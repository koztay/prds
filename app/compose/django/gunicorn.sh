#!/bin/sh
# /usr/src/app altına kopyalayınca bir app daha oluşuyor... Dolayısıyla .../app/app... olmalı path
python /usr/src/app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/usr/src/app