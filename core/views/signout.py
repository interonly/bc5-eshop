from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout


def signout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли!")
    return redirect('/')