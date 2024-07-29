from django.shortcuts import render
from core.models import Product
from django.db.models import Q


def search(request):
    keyword = request.GET["keyword"]
    products = Product.objects.filter(
        Q(name__icontains=keyword) |
        Q(description__icontains=keyword) |
        Q(category__name__icontains=keyword)
    )
    context = {"products": products}
    return render(request, 'search_result.html', context)