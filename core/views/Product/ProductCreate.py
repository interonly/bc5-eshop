from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ProductForm
from django.views import View


class ProductCreateView(View):
    def get(self, request):
        context = {}
        context["product_form"] = ProductForm()
        return render(request, 'Product/create.html', context)

    def post(self, request):
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Успешно сохранено!")
            return redirect('/product-create/')
        messages.warning(request, "Ошибка валидации формы!")