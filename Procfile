web: gunicorn pricehound.wsgi --log-file -
worker:celery -A pricehound worker --loglevel=INFO
