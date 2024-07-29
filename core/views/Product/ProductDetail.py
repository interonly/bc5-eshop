from django.shortcuts import render
from core.models import Product
from costumerapp.models import Costumer
from django.views import View


class ProductDetailView(View):
    def get(self, request, pk):
        product_object = Product.objects.get(pk=pk)
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