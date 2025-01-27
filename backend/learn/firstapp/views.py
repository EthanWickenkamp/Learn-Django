from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item


def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index")


def poop(request):
    return HttpResponse("poop")


def item_view(request):
    items = Item.objects.all() 
    context = {"items":items}
    return render(request, "firstapp/item_list.html", context)