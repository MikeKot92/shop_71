from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class CartQueryset(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = CartQueryset.as_manager()

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f'Корзина  {self.user} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        cart_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return cart_item
