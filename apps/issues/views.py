from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, RedirectView
from apps.boards.forms import BoardPositionForm
from apps.issues.models import Issue


class IssueDetailView(DetailView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['board_form'] = BoardPositionForm()
        if self.request.is_ajax():
            self.template_name = 'issues/issue_detail_ajax.html'
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