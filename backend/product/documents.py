from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product




@registry.register_document
class ProductDocument(Document):
    id = fields.IntegerField()
    name = fields.TextField(
        attr='name',
        fields={
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )
    price = fields.DoubleField()
    quantity = fields.IntegerField()
    brand = fields.TextField()


    class Index:
        name = 'product_list'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Product