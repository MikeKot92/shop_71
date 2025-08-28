import stripe
from django.conf import settings
from django.db import models

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='products_images', verbose_name='Изображение')
    stripe_product_price_id = models.CharField(max_length=64, blank=True, null=True, verbose_name='Stripe_id')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None, ):
        if not self.stripe_product_price_id:
            self.stripe_product_price_id = self.create_stripe_product_price()['id']
        super().save(*args, force_insert=False, force_update=False, using=None, update_fields=None,)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='rub',
        )
        return stripe_product_price
