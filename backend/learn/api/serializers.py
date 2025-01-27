from rest_framework import serializers
from firstapp.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description'] #'__all__' instead of array works too