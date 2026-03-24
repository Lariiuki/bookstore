from django.urls import path, include
from rest_framework import routers

from order.viewseets import OrderViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]