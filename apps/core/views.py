from django.views.generic.detail import DetailView
from apps.core.models import Board, Story


class BoardDetailView(DetailView):
    model = Board

class StoryDetailView(DetailView):
    model = Story