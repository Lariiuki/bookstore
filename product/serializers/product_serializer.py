from rest_framework import serializers

from product.models.product import Product 
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'active', 'category', 'category_id']

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')
        product = Product.objects.create(**validated_data)
        product.category.set(category_data)
        return product
