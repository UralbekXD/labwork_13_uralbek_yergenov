from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):

    class CategoryChoices(models.TextChoices):
        ELECTRONICS = 'electronics', _('электроника')
        FRUITS = 'fruits', _('фрукты')
        COSMETICS = 'cosmetics', _('косметика')
        DRINKS = 'drinks', _('напитки')
        MEAT = 'meat', _('мясо')
        OTHER = 'other', _('разное')

    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    image = models.URLField(max_length=1024, null=True, blank=True, verbose_name='Фото товара')
    amount = models.PositiveIntegerField(default=0, null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Цена')

    category = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        choices=CategoryChoices.choices,
        default=CategoryChoices.OTHER,
        verbose_name='Категория',
    )

    def __str__(self):
        return f'{self.title}'
