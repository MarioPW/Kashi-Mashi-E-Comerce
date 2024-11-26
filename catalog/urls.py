from django.urls import path
from .views import catalog, detail, cat_products

urlpatterns = [
    path('', catalog, name='catalog'),
    path('detail/<int:id>', detail, name='detail'),
    path('cat_products/<int:id>', cat_products, name='cat_products'),   
]