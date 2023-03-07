from django.urls import path

from game.views import game, games_list, main, new_game
from game.views_api import GameView, GamesView, RoundView, RoundsView


urlpatterns = [
    # Template views.
    path('', main, name='main_page_view'),
    path('games', games_list, name='games_list_page_view'),
    path('games/<int:game_id>', game, name='game'),
    path('games/new/<str:game_type>', new_game, name='new_game'),

    # Api views.
    path('api/games', GamesView.as_view(), name='api_games'),
    path('api/games/<int:game_id>', GameView.as_view(), name='api_selected_game'),
    path('api/games/<int:game_id>/rounds', RoundsView.as_view(), name='api_rounds'),
    path('api/games/<int:game_id>/rounds/<int:round_id>', RoundView.as_view(), name='api_selected_round'),
]