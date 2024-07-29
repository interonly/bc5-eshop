from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from core.forms import AuthForm


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