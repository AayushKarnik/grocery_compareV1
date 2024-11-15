from django.shortcuts import render
from .models import Product, Price

def home(request):
    return render(request, "groceries/home.html")

def product_search(request):
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    
    products = Product.objects.filter(name__icontains=query)
    prices = Price.objects.filter(product__in=products)

    if max_price:
        prices = prices.filter(price__lte=max_price)
    if location:
        prices = prices.filter(location=location)

    return render(request, 'groceries/product_search.html', {'prices': prices})