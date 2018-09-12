import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Auction.settings')

app = Celery('Auction')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send_email_to_winner': {
        'task': 'tasks.send_email',
        'schedule': crontab(minute=0, hour=0),
    },
}
