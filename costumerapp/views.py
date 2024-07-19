from django.shortcuts import render, HttpResponse
from .models import Costumer, Profile
from .forms import CostumerForm, ProfileForm


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
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")
    
def profile_view(request):
    profile_list = Profile.objects.all()
    context = {"profiles": profile_list}

    return render(request, 'profiles.html', context)

def profile_detail(request, id):
    profile_object = Profile.objects.get(id=id)
    context = {"profile": profile_object,}
    return render(request, 'profile_detail.html', context)

def profile_create(request):
    context = {}
    context["profile_form"] = ProfileForm()

    if request.method == "GET":
        return render(request, 'profile_create.html', context)
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")