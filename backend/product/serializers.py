from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Product
from .documents import ProductDocument


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'quantity',
            'price',
            'brand',
        )
        model = Product


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument

        fields = (
            'id',
            'name',
            'quantity',
            'price',
            'brand',
        )


