from rest_framework import status
from rest_framework.test import APITestCase


class TestApiRoot(APITestCase):
    def test_api_root_with_trailing_slash(self):
        response = self.client.get("/bookstore/v1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["version"], "v1")
        self.assertEqual(response.data["endpoints"]["products"], "/bookstore/v1/products/")

    def test_api_root_without_trailing_slash(self):
        response = self.client.get("/bookstore/v1")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["version"], "v1")
        self.assertEqual(response.data["endpoints"]["orders"], "/bookstore/v1/orders/")
