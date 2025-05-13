from django.test import TestCase
from product.models import Product
from product.serializers.product_serializer import ProductSerializer
from product.serializers.category_serializer import CategorySerializer

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

class TestOrder(TestCase):
    def test_order_serializer(self):
        product_data = {"title": "Livro Django", "price": 100.0}
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Livro Django")
        self.assertEqual(serializer.validated_data["price"], 100.0)

class TestCategory(TestCase):
    def test_category_serializer(self):
        category_data = {"title": "Programming", "slug": "programming", "description": "Books about programming", "active": True}
        serializer = CategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["title"], "Programming")
        self.assertEqual(serializer.validated_data["slug"], "programming")
        self.assertEqual(serializer.validated_data["description"], "Books about programming")
        self.assertTrue(serializer.validated_data["active"])
