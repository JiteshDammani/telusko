from django.shortcuts import render
from .models import Destination, DailyRecords
from django.db.models import Sum


def index(request):
    dests = Destination.objects.all()
    sum = DailyRecords.objects.filter(input='AAA-TOTAL AHD').aggregate(Sum('amount'))
    print(sum)
    return render(request, "index.html", {'dests': dests})
