from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from firstapp.models import Item, Team, Game, Player
from .serializers import ItemSerializer, TeamSerializer, GameSerializer, PlayerSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'name'


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def players(self, request, slug=None):
        team = self.get_object()
        players = team.players.all()  # using the related_name
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer