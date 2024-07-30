from django.shortcuts import render
from django.contrib.auth.models import User


def users_list(request):
    user_list = User.objects.all()
    context = {"users": user_list}
    return render(request, 'user_list.html', context)