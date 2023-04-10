# import os
# from celery import Celery
# from celery.signals import after_task_publish, task_prerun, task_postrun, task_failure
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
#
# app = Celery('core')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
import json
import os
import logging

from django import setup

from celery import Celery
from celery.signals import after_task_publish, task_prerun, task_postrun, task_failure
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
setup()
logger = logging.getLogger(__name__)

from apps.celery_log.models import CeleryLog

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@after_task_publish.connect
def log_task_sent(sender=None, headers=None, body=None, **kwargs):
    task_id = headers['id']
    task_name = headers['task']
    CeleryLog.objects.create(task_id=task_id, task_name=task_name, status='SENT')


@task_prerun.connect
def log_task_started(sender=None, task_id=None, **kwargs):
    task_name = sender.__name__
    CeleryLog.objects.filter(task_id=task_id).update(task_name=task_name, status='STARTED',
                                                     date_executed=timezone.now())


@task_postrun.connect
def log_task_finished(sender=None, task_id=None, task_return_value=None, **kwargs):
    json_body = json.dumps(kwargs.get('args', {'message': 'Not found args'}))
    CeleryLog.objects.filter(task_id=task_id).update(status='SUCCESS', result=json_body)


@task_failure.connect
def log_task_failed(sender=None, task_id=None, exception=None, traceback=None, **kwargs):
    CeleryLog.objects.filter(task_id=task_id).update(status='FAILURE', traceback=traceback)
