from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from game.domain.actions import (
    start_game,
    get_game,
    get_round,
    get_rounds,
    new_round,
    set_user_choice,
)
from game.serializers.model import RoundSerializer
from game.serializers.request import StartGameRequestSerializer, UpdateRoundRequestSerializer
from game.serializers.response import GameResponseSerializer


class GamesView(APIView):

    def post(self, request):
        req_serializer = StartGameRequestSerializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)

        game_data = start_game(
            game_type=req_serializer.validated_data['game_type'],
            player_names=req_serializer.validated_data['players'],
        )

        resp_serializer = GameResponseSerializer(game_data)

        return Response(resp_serializer.data, status=status.HTTP_201_CREATED)


class GameView(APIView):

    def get(self, request, game_id):
        game = get_game(game_id)
        serializer = GameResponseSerializer(game)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RoundsView(APIView):

    def get(self, request, game_id):
        rounds = get_rounds(game_id)
        serializer = RoundSerializer(rounds, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, game_id):
        round = new_round(game_id)
        serializer = RoundSerializer(round)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoundView(APIView):

    def get(self, request, game_id, round_id):
        round = get_round(game_id, round_id)
        serializer = RoundSerializer(round)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, game_id, round_id):
        serializer = UpdateRoundRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        set_user_choice(game_id, round_id, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
