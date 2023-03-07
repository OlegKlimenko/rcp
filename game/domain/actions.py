from django.db.models import Count
from django.db.transaction import atomic
from django.shortcuts import get_object_or_404

from game.constants import WINNER
from game.domain.choices import ChoicesRegistry
from game.models import Player, Game, GamePlayer, Round, RoundPlayerChoice


@atomic
def start_game(game_type, player_names):
    players = Player.get_or_create_players(player_names)
    game = Game.objects.create(game_type=game_type)

    for player in players:
        GamePlayer.objects.create(player=player, game=game)

    # Initialize first game round.
    round = Round.objects.create(game=game)

    return {
        'game': game,
        'players': players,
        'round': round
    }


def get_game(game_id):
    game = get_object_or_404(Game, id=game_id)
    rounds = Round.objects.filter(game=game)

    finished_rounds = rounds.filter(state=WINNER)

    winners = (
        finished_rounds.exclude(winner=None)
        .values('winner__name')
        .annotate(count=Count('winner__name'))
        .order_by()
    )

    last_round_winner = None
    if finished_rounds:
        last_round_winner = finished_rounds.order_by('-id').first()

    return {
        'game': game,
        'players': Player.objects.filter(gameplayer__game=game),
        'rounds': finished_rounds,
        'winners': winners,
        'last_round_winner': last_round_winner,
        'current_round': rounds.exclude(state=WINNER).first(),
    }


def get_all_games():
    return Game.objects.all()


def get_rounds(game_id):
    return Round.objects.filter(game__id=game_id).order_by('-id')


def get_round(game_id, round_id):
    return get_object_or_404(Round, id=round_id, game__id=game_id)


def new_round(game_id):
    game = get_object_or_404(Game, id=game_id)
    return Round.objects.create(game=game)


@atomic
def set_user_choice(game_id, round_id, player_name, choice):
    player, _ = Player.objects.get_or_create(name=player_name)
    round = get_object_or_404(Round, id=round_id, game__id=game_id)
    players_in_game = GamePlayer.objects.filter(game__id=game_id)

    RoundPlayerChoice.objects.create(round=round, player=player, option=choice)
    round_choices = RoundPlayerChoice.objects.filter(round=round)

    if players_in_game.count() == round_choices.count():
        winner_player = set_winner(round_choices)

        if winner_player:
            round.winner = winner_player

        round.state = WINNER
        round.save()

        new_round(game_id)


def set_winner(round_choices):
    if round_choices.count() != 2:
        raise ValueError('Only two players is supported at the moment')

    first_player_choice, second_player_choice = round_choices

    choice_cls_first = ChoicesRegistry.get(first_player_choice.option)
    choice_cls_second = ChoicesRegistry.get(second_player_choice.option)

    c1 = choice_cls_first(player=first_player_choice.player)
    c2 = choice_cls_second(player=second_player_choice.player)

    result = c1.compare(c2)

    if result:
        return result.player
