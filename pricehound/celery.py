from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pricehound.settings')

app = Celery('data_store')

app.conf.beat_schedule = {
    'add-every-1-hour': {
        'task': 'data_store.tasks.fetch_from_fkin',
        'schedule': crontab(minute=0,hour='*/1'),
        'args': ('')
    },
}

app.conf.timezone = 'Asia/Kolkata'
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')
#'django.conf:settings'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
#lambda:settings.INSTALLED_APPS
#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))
