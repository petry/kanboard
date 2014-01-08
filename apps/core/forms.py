from django import forms
from apps.core.models import Board, BoardPosition


class BoardPositionForm(forms.ModelForm):
    story = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = BoardPosition
        exclude = ['status']

    def save(self, commit=True):
        return super(BoardPositionForm, self).save(commit)


    def on_board(self):
        if not self.is_valid():
            return None
        board = self.cleaned_data['board']
        initial_step = board.step_set.get(initial=True)
        self.instance.status = initial_step
        return self.save()