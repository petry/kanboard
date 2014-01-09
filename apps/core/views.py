from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.core.forms import BoardPositionForm
from apps.core.models import Board, Story


class BoardListView(ListView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        context['icebox'] = Story.objects.filter(boardposition=None)
        return context


class BoardDetailView(DetailView):
    model = Board


class StoryDetailView(DetailView):
    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['board_form'] = BoardPositionForm()
        return context


class StoryAdvanceView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        story = Story.objects.get(id=self.kwargs['pk'])
        story.boardposition.go()
        return reverse('board-detail', kwargs={'pk': story.boardposition.board.id})


class StoryOnBoardView(RedirectView):
    permanent = False

    def post(self, request, *args, **kwargs):
        position_form = BoardPositionForm(
            data={
                'story': kwargs['pk'],
                'board': request.POST.get('board')
            }
        )
        position_form.on_board()
        return super(StoryOnBoardView, self).post(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        story = Story.objects.get(id=kwargs['pk'])
        return reverse('board-detail', kwargs={'pk': story.boardposition.board.id})