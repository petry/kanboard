from django.contrib import admin
from apps.core.models import Board, Story, Step, Transition

admin.site.register(Board)
admin.site.register(Story)
admin.site.register(Step)
admin.site.register(Transition)