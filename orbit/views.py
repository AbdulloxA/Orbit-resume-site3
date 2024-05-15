from django.shortcuts import render
from .models import About, Portfolio
# Create your views here.

def index(request):
    about = About.objects.all()
    portfolio = Portfolio.objects.all()
    ctx = {
        "about": about,
        "portfolio": portfolio
    }
    return render(request, 'index.html', ctx)