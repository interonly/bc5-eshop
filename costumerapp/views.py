from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Costumer
from .forms import *


def costumer_view(request):
    costumer_list = Costumer.objects.all()
    context = {"costumers": costumer_list}

    return render(request, 'costumers.html', context)

def costumer_create(request):
    context = {}
    context["costumer_form"] = CostumerForm()
    if request.method == "GET":
        return render(request, 'costumer_create.html', context)
    if request.method == "POST":
        costumer_form = CostumerForm(request.POST)
        if costumer_form.is_valid():
            costumer_form.save()
            messages.success(request, "Успешно сохранено!")
            return redirect('costumers')
        messages.warning(request, "Ошибка валидации формы")