from django.db import models
from django.utils import timezone


class CeleryLog(models.Model):
    task_id = models.CharField(max_length=50)
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)
    date_executed = models.DateTimeField(null=True, blank=True)
    result = models.TextField(null=True, blank=True)
    traceback = models.TextField(null=True, blank=True)
