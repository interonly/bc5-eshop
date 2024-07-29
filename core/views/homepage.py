from django.shortcuts import render
from core.models import Product
from core.filters import ProductFilter


def homepage(request):
    product_list = Product.objects.all()
    filter_object = ProductFilter(
        data = request.GET,
        queryset = product_list
    )
    context = {"filter_object": filter_object}
    return render(request, 'index.html', context)