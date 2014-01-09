from django import forms
from apps.core.models import Board, BoardPosition, Story


class BoardPositionForm(forms.ModelForm):
    board = forms.ModelChoiceField(
        queryset=Board.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BoardPosition
        exclude = ['status', 'story']

    def on_board(self):
        if not self.is_valid():
            return None
        board = self.cleaned_data['board']
        initial_step = board.step_set.get(initial=True)
        self.instance.story = Story.objects.get(id=self.data['story'])
        self.instance.status = initial_step
        return self.save()