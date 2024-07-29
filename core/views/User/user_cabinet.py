from django.shortcuts import render
from django.contrib.auth.models import User


def user_cabinet(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'cabinet.html', context)