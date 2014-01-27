from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from apps.boards.models import Board
from apps.issues.models import Issue


class BoardListView(ListView):
    model = Board

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        context['icebox'] = Issue.objects.filter(boardposition=None)
        return context


class BoardDetailView(DetailView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        steps = self.object.step_set.count()
        if steps:
            context['panel_size_class'] = "col-md-{0}".format(12/steps)

        return context


class BoardReportView(ListView):
    model = Issue
    template_name = 'boards/board_report.html'
    board = None

    def get(self, request, *args, **kwargs):
        self.queryset = Issue.objects.filter(boardposition__board=kwargs['pk'])
        self.board = Board.objects.get(id=kwargs['pk'])
        return super(BoardReportView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardReportView, self).get_context_data(**kwargs)
        context['board'] = self.board
        return context