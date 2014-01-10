from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.core.forms import BoardPositionForm
from apps.core.models import Board, Issue


class BoardListView(ListView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        context['icebox'] = Issue.objects.filter(boardposition=None)
        return context


class BoardDetailView(DetailView):
    model = Board


class IssueDetailView(DetailView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['board_form'] = BoardPositionForm()
        return context


class IssueAdvanceView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        issue = Issue.objects.get(id=self.kwargs['pk'])
        issue.boardposition.go()
        return reverse('board-detail', kwargs={'pk': issue.boardposition.board.id})


class IssueOnBoardView(RedirectView):
    permanent = False

    def post(self, request, *args, **kwargs):
        position_form = BoardPositionForm(
            data={
                'issue': kwargs['pk'],
                'board': request.POST.get('board')
            }
        )
        position_form.on_board()
        return super(IssueOnBoardView, self).post(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs['pk'])
        return reverse('board-detail', kwargs={'pk': issue.boardposition.board.id})