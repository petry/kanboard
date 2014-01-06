from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.core.models import Board, Story


class BoardListView(ListView):
    model = Board

class BoardDetailView(DetailView):
    model = Board

class StoryDetailView(DetailView):
    model = Story