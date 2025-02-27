from django.db import models
from django.db.models import Q, Sum
from django.utils.text import slugify

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    def get_players(self):
        return self.players.all()

    def get_games(self):
        return Game.objects.filter(Q(home_team=self) | Q(away_team=self))


class Game(models.Model):
    game_date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_games", null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_games", null=True, blank=True)
    home_team_score = models.PositiveIntegerField(default=0)
    away_team_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} on {self.game_date}"

    @property
    def winner(self):
        if self.home_team_score > self.away_team_score:
            return self.home_team
        elif self.away_team_score > self.home_team_score:
            return self.away_team
        return None

    @property
    def loser(self):
        if self.winner == self.home_team:
            return self.away_team
        elif self.winner == self.away_team:
            return self.home_team
        return None

class Player(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    games_played = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.team.name})"

class Stats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="stats")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="stats")
    hits = models.PositiveIntegerField(default=0)
    runs = models.PositiveIntegerField(default=0)
    rbis = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} stats for {self.game}"

    @property
    def total_hits(self):
        return AtBat.objects.filter(player=self.player, game=self.game, outcome__in=["SINGLE", "DOUBLE", "TRIPLE", "HOMERUN"]).count()

    @property
    def total_rbis(self):
        return AtBat.objects.filter(player=self.player, game=self.game).aggregate(Sum('rbis'))['rbis__sum'] or 0

class AtBat(models.Model):
    OUTCOMES = [
        ("OUT_3", "3 Strikes and Out"),
        ("OUT_2", "2 Strikes and Out"),
        ("OUT_1", "1 Strike and Out"),
        ("OUT_0", "0 Strikes and Out"),
        ("SINGLE", "Single (1 Base Hit)"),
        ("DOUBLE", "Double (2 Base Hits)"),
        ("TRIPLE", "Triple (3 Base Hits)"),
        ("HOMERUN", "Home Run"),
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="at_bats")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="at_bats")
    inning = models.PositiveIntegerField()
    strikes = models.PositiveIntegerField(default=0)
    outcome = models.CharField(max_length=10, choices=OUTCOMES)

    def __str__(self):
        return f"{self.player.name} - {self.get_outcome_display()} in inning {self.inning}"

    @property
    def is_hit(self):
        return self.outcome in ["SINGLE", "DOUBLE", "TRIPLE", "HOMERUN"]
