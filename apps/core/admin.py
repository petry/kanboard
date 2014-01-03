from django.contrib import admin
from apps.core.models import Board, Story, Step, Transition


class StepInline(admin.TabularInline):
    model = Step
    extra = 0

class StoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'board']

class BoardAdmin(admin.ModelAdmin):
    inlines = [StepInline]

admin.site.register(Board, BoardAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Transition)