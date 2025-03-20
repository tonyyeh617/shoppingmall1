from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, Inventory

# def homepage(request):
#     product_types = ProductType.objects.all()
#     return render(request, 'homepage.html', {'product_types': product_types, 'view_name': 'homepage'})

    
from django.shortcuts import render
from .models import ProductType, ProductImage

def homepage(request):
    product_types = ProductType.objects.all()
    product_images = ProductImage.objects.all()  # Fetching all product images
    return render(request, 'homepage.html', {'product_types': product_types, 'product_images': product_images})

# def product_list(request, type_id):
#     product_type = get_object_or_404(ProductType, id=type_id)
#     products = Product.objects.filter(type=product_type)
#     return render(request, 'product_list.html', {'product_type': product_type, 'products': products, 'view_name': 'product_list'})

def product_list(request, type_id):
    product_type = get_object_or_404(ProductType, id=type_id)
    sort_by = request.GET.get('sort_by', 'name')
    order = request.GET.get('order', 'asc')
    
    if sort_by == 'price':
        if order == 'asc':
            products = Product.objects.filter(type=product_type).order_by('price')
        else:
            products = Product.objects.filter(type=product_type).order_by('-price')
    else:
        if order == 'asc':
            products = Product.objects.filter(type=product_type).order_by('name')
        else:
            products = Product.objects.filter(type=product_type).order_by('-name')

    return render(request, 'product_list.html', {'product_type': product_type, 'products': products, 'view_name': 'product_list', 'sort_by': sort_by, 'order': order})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product, 'view_name': 'product_detail'})

# from django.db.models import Q
# def search_results(request):
#     query = request.GET.get('q')
#     products = Product.objects.filter(
#         Q(name__icontains=query) | Q(description__icontains=query)
#     )
#     return render(request, 'search_results.html', {'products': products, 'query': query, 'view_name': 'search_results'})

from django.db.models import Q

def search_results(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'name')
    order = request.GET.get('order', 'asc')
    
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    
    if sort_by == 'price':
        products = products.order_by('price' if order == 'asc' else '-price')
    else:
        products = products.order_by('name' if order == 'asc' else '-name')
    
    return render(request, 'search_results.html', {'products': products, 'query': query, 'sort_by': sort_by, 'order': order, 'view_name': 'search_results'})

