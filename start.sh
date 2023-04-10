#!/bin/bash

# Esperar o RabbitMQ estar disponível
./wait-for-it.sh rabbitmq:5672

# Iniciar o servidor Django
python manage.py runserver 0.0.0.0:8000 &

# Iniciar o Celery em segundo plano
celery -A core worker -l info