from django.shortcuts import render
from .models import Costumer

# Create your views here.
def costumer_view(request):
    # SELECT * FROM Customer;
    costumer_list = Costumer.objects.all()
    context = {"costumers": costumer_list}

    return render(request, 'costumers.html', context)