from django.contrib import admin

from game.models import Player, Game, GamePlayer, Round, RoundPlayerChoice


class PlayerAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass


class GamePlayerAdmin(admin.ModelAdmin):
    pass


class RoundAdmin(admin.ModelAdmin):
    pass


class RoundPlayerChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GamePlayer, GamePlayerAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(RoundPlayerChoice, RoundPlayerChoiceAdmin)
