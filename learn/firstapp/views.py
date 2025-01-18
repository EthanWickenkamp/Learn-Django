from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Item


def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index")


def poop(request):
    return HttpResponse("poop")


def item_view(request):
    # Query all items and create python object items
    items = Item.objects.all() # can call many useful django data funct instead of all()
    
    #cleaner way to map python object to template variable
    context = {"items":items}
    # Render the template with the queried items
    return render(request, "firstapp/item_list.html", context)