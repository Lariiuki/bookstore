from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order {self.order_number} - {self.customer_name}"