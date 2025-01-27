from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from firstapp.models import Item
from .serializers import ItemSerializer
    

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer