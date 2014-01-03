from django.contrib import admin
from apps.core.models import Board, Story, Step, Transition


class StepAdmin(admin.ModelAdmin):
    list_display = ['name', 'board', 'next']


class StoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'board']


admin.site.register(Board)
admin.site.register(Story, StoryAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Transition)