from django.views.generic.detail import DetailView
from apps.core.models import Board


class BoardDetailView(DetailView):
    model = Board