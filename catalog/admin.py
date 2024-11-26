from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display_links = ('category',)
    list_display = ('category', 'show_it')
    list_editable = ('show_it',)

#Panel Configuration
@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'price', 'promo', 'new', 'category', 'sold', 'available_amount')
    list_editable = ('price', 'promo', 'new', 'category', 'sold', 'available_amount')
    search_fields = ('name', 'category')

admin.site.site_header = 'Kashi-Mashi Admin'
admin.site.site_title = 'Kashi-Mashi Admin'
admin.site.index_title = 'Admin Panel'
