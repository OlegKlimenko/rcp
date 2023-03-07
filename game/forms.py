from django import forms


class StartPPGameForm(forms.Form):
    player1 = forms.CharField(max_length=64)
    player2 = forms.CharField(max_length=64)


class StartPCGameForm(forms.Form):
    player = forms.CharField(max_length=64)
