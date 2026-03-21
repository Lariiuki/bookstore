from rest_framework import serializers
from django.utils.text import slugify

from product.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'description', 'active']
        extra_kwargs = {'slug': {'required': False}}

    def create(self, validated_data):
        if not validated_data.get('slug') and validated_data.get('title'):
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)