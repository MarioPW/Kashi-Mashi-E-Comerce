from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField, BooleanField, DateTimeField, AutoField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import locale


class Category(models.Model):
    id = AutoField(primary_key=True)
    category = CharField(max_length=100, unique=True, null=False)
    show_it = BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) -> str:
        return self.category
        
class Product(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    description  = TextField(null=False)
    price = IntegerField(blank=False)
    promo = IntegerField(default=0)
    new = BooleanField(default=False)
    sold = BooleanField(default=False)
    available_amount = IntegerField(default=0, verbose_name='Cantidad Disponible')
    category = ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    image = ImageField(upload_to='products', default = None)
    created_at = DateTimeField(default=timezone.now, null=True, verbose_name="Creation Date")
    updated_at = DateTimeField(default=timezone.now, null=True, verbose_name="Update Date")
    

    def formatted_price(self):
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        return locale.format("%d", self.price, grouping=True)

    def formatted_promo(self):
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        return locale.format("%d", self.promo, grouping=True)
     
    def __str__(self):
        return str(self.name)
