from django.shortcuts import render, redirect
from core.models import Product
from django.contrib import messages
from core.forms import ProductForm


def product_update(request, id):
    context = {}
    product_object = Product.objects.get(id=id)
    context["product_form"] = ProductForm(instance=product_object)

    if request.method == "GET":
        return render(request, "Product/update.html", context)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно обновлено!")
            return redirect('homepage')
        messages.warning(request, "Ошибка валидации формы!")