from django.http import HttpResponse
from django.shortcuts import render

from .models import Items
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Items.objects.all()
    return render(request, 'auction/index.html', {"items": items})

def create_item(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, 'auction/create-item.html', {"form": form})
    if request.method == "POST":
        bounded_form = ItemForm(request.POST)
        if bounded_form.is_valid():
            name = bounded_form.cleaned_data['name']
            description = bounded_form.cleaned_data['description']
            print(name, description, request.FILES)
            return HttpResponse('Create a new item')
        else:
            return HttpResponse(bounded_form.errors)