from django.http import HttpResponse
from django.shortcuts import render

from .models import Items

# Create your views here.
def index(request):
    items = Items.objects.all()
    return render(request, 'auction/index.html', {"items": items})