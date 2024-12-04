from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator

def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)
    return render(request, 'catalog.html', {'products': page_products,
                                    'categories': categories })

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product':product})

def cat_products(request, id):
    cat_products = Product.objects.filter(category_id=id)
    current_category = Category.objects.get(id=id)
    return render(request, 'categories.html', {'cat_products': cat_products,
                                                'category': current_category })

                                                
