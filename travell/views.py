from django.shortcuts import render, get_object_or_404
from .models import Destination
# import pandas as pd

def home(request):
    term = request.GET.get("search")
    if term:
        places = Destination.objects.filter(name__icontains=term)
    else:
        places = Destination.objects.all()
    return render(request, 'home.html',{'term':term, 'places':places})

def details(request,dest_id):
    place = get_object_or_404(Destination, pk=dest_id)
    return render(request,'details.html',{'place':place})