import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Explicitly set the broker URL to Redis
CELERY_BROKER_URL = 'redis://localhost:6379/1'
celery.conf.broker_url = CELERY_BROKER_URL

# Disable result backend if not needed
celery.conf.result_backend = None

celery.autodiscover_tasks()
