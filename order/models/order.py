from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ManyToManyField('product.Product', related_name='orders', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order #{self.pk}"