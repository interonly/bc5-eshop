from django.shortcuts import render, HttpResponse
from .models import Product
from costumerapp.models import Costumer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import *
from .filters import ProductFilter

def homepage(request):
    product_list = Product.objects.all()
    filter_object = ProductFilter(
        data = request.GET,
        queryset = product_list
    )
    context = {"filter_object": filter_object}
    return render(request, 'index.html', context)

def search(request):
    keyword = request.GET["keyword"]
    products = Product.objects.filter(
        Q(name__icontains=keyword) |
        Q(description__icontains=keyword) |
        Q(category__name__icontains=keyword)
    )
    context = {"products": products}
    return render(request, 'search_result.html', context)

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
    context = { "product": product_object}
    return render(request, 'Product/detail.html', context)

def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'Product/create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")
    
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
            return HttpResponse("Успешно обновлено!")
        return HttpResponse("Ошибка валидации!")

def user_cabinet(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'cabinet.html', context)

def users_list(request):
    user_list = User.objects.all()
    context = {"users": user_list}
    return render(request, 'user_list.html', context)

def profile_create(request):
    context = {}
    context["form"] = ProfileForm()
    
    if request.method == "GET":
        return render(request, 'profile/create.html', context)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")

def profile_update(request, id):
    context = {}
    profile_object = Profile.objects.get(id=id)
    context["form"] = ProfileForm(instance=profile_object)
    
    if request.method == "GET":
        return render(request, "profile/update.html", context)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_object)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно обновлено!")
        return HttpResponse("Ошибка валидации!")