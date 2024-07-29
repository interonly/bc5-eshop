from django.shortcuts import render
from news.models import New
from costumerapp.models import Costumer
from django.views import View

class NewDetailView(View):
    def get(self, request, pk):
        news_object = New.objects.get(pk=pk)
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