from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from firstapp.models import Item
from .serializers import ItemSerializer

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, Svelte!"})
    

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer