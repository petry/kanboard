from django import forms
from apps.core.models import Board, BoardPosition


class OnBoardForm(forms.Form):
    story = forms.CharField(widget=forms.HiddenInput)
    board = forms.ModelChoiceField(
        queryset=Board.objects.all()
    )
