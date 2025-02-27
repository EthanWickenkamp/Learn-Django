from rest_framework import serializers
from firstapp.models import Item, Team, Game, Player

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description'] #'__all__' instead of array works too


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'slug']

class GameSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)
    class Meta:
        model = Game
        fields = ['game_date', 'home_team', 'away_team', 'home_team_score', 'away_team_score']

class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Player
        fields = ['name', 'team']