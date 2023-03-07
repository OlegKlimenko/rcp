from rest_framework import serializers

from game.models import (
    Player,
    Game,
    Round,
)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_type')


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ('id', 'game', 'state', 'winner')
