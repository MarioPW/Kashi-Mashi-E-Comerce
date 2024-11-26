from django.db import models
from django.db.models.fields import CharField, TextField, AutoField, DateTimeField, IntegerField, EmailField
from django.db.models.fields.files import ImageField
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Carousel_Stuff(models.Model):
    image_name = CharField(max_length=20)
    message = CharField(max_length=100)
    image = ImageField(upload_to='carousel_images')   
    def __str__(self) -> str:
        return self.image_name

class Message(models.Model):
    id = AutoField(primary_key=True)
    customer_email = CharField(max_length=20, verbose_name='Déjanos tu e-mail')
    message = TextField(null=False, verbose_name='Cuentanos tu idea')
    image = ImageField(upload_to='customer_images', null=True, blank=True, verbose_name='Puedes enviarnos una imagen de guía acá:')
    sended_at = DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return f'from: {self.customer_email} ..... {self.sended_at}'

class Order(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100, null=False)
    price = IntegerField(blank=False)
    sended_at = DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.name} {self.sended_at}'

class Frequent_Questions(models.Model):
    id = AutoField(primary_key=True)
    question = TextField(null=False)
    answer = TextField(null=False)
    def __str__(self) -> str:
        return self.question

class Payment_Methods(models.Model):
    id = AutoField(primary_key=True)
    method = TextField(null=False)
    def __str__(self) -> str:
        return self.method

class Another_Equal(models.Model):
    id = AutoField(primary_key=True)
    customer_email = EmailField(null=False, verbose_name='Déjanos tu e-mail')
    product_ref = CharField(default='product_name', max_length=50, verbose_name='Han requerido nuevamente el producto:')
    sended_at = DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'From: {self.customer_email} ..... {self.sended_at}'

@receiver(post_delete, sender=(Carousel_Stuff))
def delete_image_Carousel(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

@receiver(post_delete, sender=(Message))
def delete_image_Message(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)