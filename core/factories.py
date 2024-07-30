import factory
from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f'test name {n}')
    price = factory.Sequence(lambda n: f'{n}')
    qty = factory.Sequence(lambda n: f'{n}')
