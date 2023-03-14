from django.db import models

from products.models import Product


# Create your models here.
class ProductInCart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='products_in_cart',
        verbose_name='Товар',
    )

    quantity = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
        verbose_name='Количество',
    )

    def __str__(self):
        return f'{self.product.title} {self.quantity}'


