from django.db import models

from store.models import Product

# Create your models here.
class Cart(models.Model):
    card_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.card_id
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=True)

    def __str__(self):
        return self.product