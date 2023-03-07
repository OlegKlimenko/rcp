from rest_framework import serializers

from game.constants import (
    PLAYER_VS_PLAYER,
    PLAYER_VS_COMPUTER,
    OPTION_ROCK,
    OPTION_PAPER,
    OPTION_SCISSORS,
)


class StartGameRequestSerializer(serializers.Serializer):
    GAME_TYPE_CHOICES = (
        PLAYER_VS_PLAYER, PLAYER_VS_COMPUTER
    )

    game_type = serializers.ChoiceField(choices=GAME_TYPE_CHOICES)
    players = serializers.ListSerializer(
        child=serializers.CharField(max_length=64), allow_empty=False
    )


class UpdateRoundRequestSerializer(serializers.Serializer):
    PLAYER_ROUND_CHOICES = (
        OPTION_ROCK, OPTION_PAPER, OPTION_SCISSORS
    )

    player_name = serializers.CharField(max_length=64)
    choice = serializers.ChoiceField(choices=PLAYER_ROUND_CHOICES)
