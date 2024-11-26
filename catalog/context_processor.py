from catalog.models import Product, Category

def get_product(request):
    new_product = Product.objects.all()
    return {'products': new_product}

def get_category(request):
    new_category = Category.objects.all()
    return {'categories': new_category}