from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.core.models import Board, Story


class BoardListView(ListView):
    model = Board

class BoardDetailView(DetailView):
    model = Board

class StoryDetailView(DetailView):
    model = Story

class StoryAdvanceView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        story = Story.objects.get(id=1)
        return reverse('board-detail', kwargs={'pk': story.boardposition.board.id})
