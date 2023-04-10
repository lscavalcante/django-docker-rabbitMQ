# Django with RabbitMQ and Celery on Docker Compose
This is a project template for running a Django application with RabbitMQ and Celery using Docker Compose.

## Installation
1. Install Docker and Docker Compose.
2. Clone this repository:

```
$ git clone https://github.com/lscavalcante/django-docker-rabbitMQ.git
$ cd your-repo 
```


3. Build and run the application using Docker Compose:
```
$ docker-compose up --build 
```

4. Access the application in a web browser at 
   - Django - http://localhost:8000/api/v1/
   - RabbitMQ - http://localhost:5672


## Configuration
The following environment variables can be set in the docker-compose.yml file:

## Django
- CELERY_BROKER_URL: URL for the RabbitMQ broker, default is amqp://guest:guest@rabbitmq:5672//
- CELERY_RESULT_BACKEND: Result backend URL, default is django-db://sqlite:///db.sqlite3
- CELERY_RESULT_DBURI: Result backend URL for Celery 5, default is django-db://sqlite:///db.sqlite3
- CELERY_CACHE_BACKEND: Cache backend, default is django-cache 

## RabbitMQ
- RABBITMQ_DEFAULT_USER: Default user for RabbitMQ, default is guest
- RABBITMQ_DEFAULT_PASS: Default password for RabbitMQ, default is guest
