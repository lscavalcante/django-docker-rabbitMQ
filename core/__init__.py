# Importe o aplicativo Celery
from .celery import app as celery_app

# Defina o nome do aplicativo quando importado
__all__ = ('celery_app',)