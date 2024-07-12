from django.shortcuts import render, HttpResponse
from .models import Product
from costumerapp.models import Costumer


def homepage(request):
    product_list = Product.objects.all()
    context = {"products": product_list}

    return render(request, 'index.html', context)


def product_detail(request, id):
    product_object = Product.objects.get(id=id)

    product_object.views_qty += 1
    if request.user.is_authenticated:
        user = request.user
        if not Costumer.objects.filter(user=user).exists():
            costumer = Costumer.object.create(
                name=user.username,
                age=0,
                gender='-',
                user=user
            )
        costumer = user.costumer
        product_object.costumer_views.add(costumer)

    product_object.save()

    context = {
        "product": product_object,
    }
    return render(request, 'product_detail.html', context)

