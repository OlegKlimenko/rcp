from game.domain.choices.choices import RockChoice, PaperChoice, ScissorsChoice


class ChoicesRegistry:
    choices_classes = {}

    @classmethod
    def register(cls, choice_cls):
        cls.choices_classes[choice_cls.option] = choice_cls

    @classmethod
    def get(cls, option):
        return cls.choices_classes.get(option)


ChoicesRegistry.register(RockChoice)
ChoicesRegistry.register(PaperChoice)
ChoicesRegistry.register(ScissorsChoice)
