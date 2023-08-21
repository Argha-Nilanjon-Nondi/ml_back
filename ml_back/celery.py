"""
create a celery app
"""

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ml_back.settings")
app = Celery("ml_back")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()