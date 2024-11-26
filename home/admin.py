from django.contrib import admin

from .models import Carousel_Stuff, Message, Order, Frequent_Questions, Payment_Methods, Another_Equal

admin.site.register(Carousel_Stuff)
admin.site.register(Message)
admin.site.register(Frequent_Questions)
admin.site.register(Payment_Methods)
admin.site.register(Another_Equal)

@admin.register(Order)
class Product_Admin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'price', 'sended_at')
    search_fields = ('name', 'sended_at')