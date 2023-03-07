from abc import ABC, abstractmethod

from game.constants import OPTION_ROCK, OPTION_PAPER, OPTION_SCISSORS


class Choice(ABC):
    option: str

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def compare(self, other):
        pass


class RockChoice(Choice):
    option = OPTION_ROCK

    def compare(self, other):
        if isinstance(other, ScissorsChoice):
            return self
        if isinstance(other, PaperChoice):
            return other
        return None


class PaperChoice(Choice):
    option = OPTION_PAPER

    def compare(self, other):
        if isinstance(other, RockChoice):
            return self
        if isinstance(other, ScissorsChoice):
            return other
        return None


class ScissorsChoice(Choice):
    option = OPTION_SCISSORS

    def compare(self, other):
        if isinstance(other, PaperChoice):
            return self
        if isinstance(other, RockChoice):
            return other
        return None
