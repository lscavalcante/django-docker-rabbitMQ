from django.contrib import admin

from apps.celery_log.models import CeleryLog

admin.site.register(CeleryLog)
