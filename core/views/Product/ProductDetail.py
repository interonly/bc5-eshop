from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Product
from costumerapp.models import Costumer
from django.views import View


class ProductDetailView(View):
    def get(self, request, pk):
        try:
            product_object = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            messages.error(request, "Такого товара не существует!")
            return redirect('homepage')
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
        context = { "product": product_object}
        return render(request, 'Product/detail.html', context)