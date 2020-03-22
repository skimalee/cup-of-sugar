from django.shortcuts import render
from . models import Cup

# Create your views here.
def home(request):
    return render(request, 'home.html')