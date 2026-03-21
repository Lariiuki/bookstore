from rest_framework import serializers

from product.models.product import Product 
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(source='categories', read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='categories', queryset=Category.objects.all(), write_only=True, many=True, required=False
    )

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'active', 'category', 'category_id']
