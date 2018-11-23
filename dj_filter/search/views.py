from django.shortcuts import render
from .filters import ProductFilter
from .models import Product

# Create your views here.
def search_product(request):
    template = 'search/product.html'
    product = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product)
    context = {"product_filter": product_filter}
    return render(request, template, context)
