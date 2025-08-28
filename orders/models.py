from django.db import models

from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=256, verbose_name='Почта')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    cart_history = models.JSONField(default=dict, verbose_name='Покупки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES, verbose_name='Статус')
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Заказчик')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ #{self.id} {self.first_name} {self.last_name}'

    def order_items_history(self, carts):
        self.cart_history = {
            'items': [cart.de_json() for cart in carts],
            'total_sum': float(carts.total_sum()),
            'quantity': carts.total_quantity(),
        }
        carts.delete()
        self.save()
