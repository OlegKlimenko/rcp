from rest_framework import serializers

from game.serializers.model import GameSerializer, PlayerSerializer, RoundSerializer


class GameResponseSerializer(serializers.Serializer):
    game = GameSerializer()
    players = PlayerSerializer(many=True)
    round = RoundSerializer()
