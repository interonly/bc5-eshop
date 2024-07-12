from django.shortcuts import render
from .models import New
from costumerapp.models import Costumer


def news_view(request):
    news_list = New.objects.all()
    context = {"news": news_list}

    return render(request, 'news.html', context)


def news_detail(request, id):
    news_object = New.objects.get(id=id)

    news_object.views += 1
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
        news_object.user_views.add(user)

    news_object.save()

    context = {
        "new": news_object,
    }
    return render(request, 'news_detail.html', context)

