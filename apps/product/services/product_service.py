import time

from celery import shared_task

from apps.product.models import Product


@shared_task(name='create_product_task')
def create_product_task(validated_data):
    Product.objects.all().delete()
    Product.objects.create(**validated_data)

