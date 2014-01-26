from django import forms
from apps.boards.models import Board, BoardPosition, Transition
from apps.issues.models import Issue

__author__ = 'petry'


class BoardPositionForm(forms.ModelForm):
    board = forms.ModelChoiceField(
        queryset=Board.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BoardPosition
        exclude = ['status', 'issue', 'show']

    def on_board(self):
        if not self.is_valid():
            return None
        board = self.cleaned_data['board']
        initial_step = board.step_set.get(initial=True)
        self.instance.issue = Issue.objects.get(id=self.data['issue'])
        self.instance.status = initial_step
        Transition.objects.create(issue=self.instance.issue, step=initial_step)

        return self.save()