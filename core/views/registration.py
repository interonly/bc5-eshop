from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import RegistrationForm


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