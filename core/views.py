from django.shortcuts import render, HttpResponse
from .models import Product
from costumerapp.models import Costumer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import ProductForm

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

def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'product_create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")

def users_page(request):
    User = get_user_model()
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'users.html', context)

def user_detail(request, id):
    user_data = User.objects.get(id=id)
    context = {"user": user_data}
    return render(request, 'user_detail.html', context)