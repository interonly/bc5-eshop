from django.shortcuts import render, redirect
from django.contrib import messages
from news.models import New
from django.views import View


class NewCreateView(View):
    def get(self, request):
        return render(request, 'new_create.html')
    def post(self, request):
        data = request.POST
        title = data["new_title"]
        article = data["new_article"]
        new_object = New.objects.create(
            title=title,
            article=article,
        )
        messages.success(request, "Успешно сохранено!")
        return redirect("news")