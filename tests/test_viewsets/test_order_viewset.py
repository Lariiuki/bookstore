import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from order.models import Order
from product.models import Product

class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='technolgy')
        self.product = ProductFactory(title='mouse', price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['product'][0]['price'], str(self.product.price))
        self.assertEqual(order_data['product'][0]['category'][0]['title'], self.category.title)

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({
            'user': user.id,
            'product_id': [product.id]
        })

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=data,
            format='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)