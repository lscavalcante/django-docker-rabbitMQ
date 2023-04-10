from django.shortcuts import render
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from apps.product.models import Product
from apps.product.services.product_service import create_product_task


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAPI(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # create_product_task.delay(serializer.validated_data)
        # ProductService.create_product_task.delay(serializer.validated_data)
        # create_product_task.apply_async(args=[serializer.validated_data], queue='django-rabbitmq')
        # create_product_task.apply_async(args=[serializer.validated_data], queue='queue_lucas')
        create_product_task.apply_async(args=[serializer.validated_data])

        return Response({'create with sucess'}, 201)
