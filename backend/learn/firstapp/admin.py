from django.contrib import admin

# Register your models here.
from .models import Item, Player, Team, Game
admin.site.register(Item)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
