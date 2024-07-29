from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from costumerapp.models import Costumer
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db.models import Q
from .forms import *
from .filters import ProductFilter
from django.views import View

def registration(request):
    context = {}
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user_object = reg_form.save()
            password = request.POST["password"]
            user_object.set_password(password)
            user_object.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('/')
        else:
            messages.warning(request, "Ошиба валидации")

    reg_form = RegistrationForm()
    context["reg_form"] = reg_form
    return render(request, 'profile/registration.html', context)

def signin(request):
    context = {}
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Вы успешно авторизовались!")
                return redirect('/')
            messages.warning(request, "Логин и/или пароль не верны")
        else:
            messages.warning(request, "Данные не валидны")

    signin_form = AuthForm()
    context["form"] = signin_form
    return render(request, 'profile/signin.html', context)
            
def signout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли!")
    return redirect('/')
                    
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

def user_cabinet(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'cabinet.html', context)

def users_list(request):
    user_list = User.objects.all()
    context = {"users": user_list}
    return render(request, 'user_list.html', context)

class ProfileCreateView(View):
    def get(self, request):
        context = {}
        context["form"] = ProfileForm()
        return render(request, 'profile/create.html', context)
    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно сохранено!")
            return redirect('users')
        messages.warning(request, "Ошибка валидации формы!")

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
            messages.success(request, "Успешно обновлено!")
            return redirect(f"users")
        messages.warning(request, "Ошибка валидации формы!")