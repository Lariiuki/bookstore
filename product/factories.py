import factory

from django.contrib.auth.models import User
from product.models import Product, Category
from order.models import Order

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Faker('boolean')

    class Meta:
        model = User

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Order