from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ProfileForm, Profile


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