web: gunicorn pricehound.wsgi --log-file -
worker: celery -A pricehound worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
