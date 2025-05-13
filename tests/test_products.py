from django.test import TestCase
from product.models import Product
from product.serializers import ProductSerializer

class TestProduct(TestCase):
    def test_str_representation(self):
        product = Product(title="Livro Django")
        self.assertEqual(str(product), "Livro Django")

    def test_product_serializer(self):
        product_data = {"title": "Livro Django", "price": 100.0}
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Livro Django")
        self.assertEqual(serializer.validated_data["price"], 100.0)