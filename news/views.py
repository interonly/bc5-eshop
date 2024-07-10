from django.shortcuts import render
from .models import New

# Create your views here.
def news_view(request):
    # SELECT * FROM New;
    news_list = New.objects.all()
    context = {"news": news_list}

    return render(request, 'news.html', context)