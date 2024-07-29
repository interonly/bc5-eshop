from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ProfileForm
from django.views import View


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