from .models import Product
from django import forms
import django_filters

class ProductFilter(django_filters.FilterSet):
    # please don't use the keyword of 'name'.
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter()

    class Meta:
        model = Product
        fields = '__all__'
        # fields = {'name', 'price',}
