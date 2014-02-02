from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, RedirectView
from django.views.generic.edit import CreateView
from apps.boards.forms import BoardPositionForm
from apps.core.mixins import ProtectedViewMixin
from apps.issues.forms import IssueForm
from apps.issues.models import Issue


class IssueCreateView(ProtectedViewMixin, CreateView):
    model = Issue
    form_class = IssueForm

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            self.template_name_suffix = '_form_ajax'
        return super(IssueCreateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('board-list')


class IssueDetailView(ProtectedViewMixin, DetailView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['board_form'] = BoardPositionForm()
        if self.request.is_ajax():
            self.template_name_suffix = '_detail_ajax'
        return context


class IssueAdvanceView(ProtectedViewMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        issue = Issue.objects.get(id=self.kwargs['pk'])
        issue.boardposition.go()
        return reverse('board-detail', kwargs={'pk': issue.boardposition.board.id})


class IssueOnBoardView(ProtectedViewMixin, RedirectView):
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
