from typing import List

from django.db import models

from game import constants


class Player(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    @staticmethod
    def get_or_create_players(player_names: List[str]):
        players = []

        for player_name in player_names:
            player, _ = Player.objects.get_or_create(name=player_name)
            players.append(player)

        return players


class Game(models.Model):
    GAME_TYPES = (
        (constants.PLAYER_VS_PLAYER, 'Player VS Player'),
        (constants.PLAYER_VS_COMPUTER, 'Player VS Computer')
    )

    game_type = models.CharField(choices=GAME_TYPES, max_length=2)

    def __str__(self):
        return str(self.id)


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player} / {self.game}"

    class Meta:
        unique_together = ('player', 'game')


class Round(models.Model):
    ROUND_STATES = (
        (constants.PLAYERS_TURN, 'Players turn'),
        (constants.WINNER, 'Winner'),
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    state = models.CharField(choices=ROUND_STATES, default=constants.PLAYERS_TURN, max_length=2)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Round #{self.id}, Game #{self.game.id}"


class RoundPlayerChoice(models.Model):
    PLAYER_CHOICES = (
        (constants.OPTION_ROCK, 'Rock'),
        (constants.OPTION_PAPER, 'Paper'),
        (constants.OPTION_SCISSORS, 'Scissors'),
    )

    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    option = models.CharField(choices=PLAYER_CHOICES, max_length=1)

    def __str__(self):
        return f"{self.round} / {self.player} / {self.option}"

    class Meta:
        unique_together = ('round', 'player', 'option')
