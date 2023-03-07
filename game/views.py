from django.shortcuts import redirect, render
from django.http.response import Http404, HttpResponse

from rest_framework.status import HTTP_400_BAD_REQUEST

from game.constants import PLAYER_VS_PLAYER, PLAYER_VS_COMPUTER
from game.domain.actions import get_all_games, get_game, start_game
from game.forms import StartPPGameForm


def main(request):
    return render(request, 'main.html')


def games_list(request):
    return render(request, 'games_list.html', {'games': get_all_games()})


def game(request, game_id):
    return render(request, 'game.html', {**get_game(game_id)})


def new_game(request, game_type):
    if request.method == 'GET':
        if game_type not in [PLAYER_VS_PLAYER, PLAYER_VS_COMPUTER]:
            return Http404('Not found game type')

        template = 'new_game_pp.html' if game_type == PLAYER_VS_PLAYER else 'new_game_pc.html'

        return render(request, template, {'game_type': game_type})

    elif request.method == 'POST':
        form = StartPPGameForm(request.POST)
        form.is_valid()

        new_game = start_game(
            game_type,
            [form.cleaned_data['player1'], form.cleaned_data['player2']]
        )
        game_id = new_game['game'].id

        return redirect('game', game_id=game_id)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)
