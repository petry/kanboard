from django.contrib import admin
from apps.boards.models import BoardPosition, Transition
from apps.issues.models import Issue


class PositionInline(admin.TabularInline):
    model = BoardPosition


class TransitionInline(admin.TabularInline):
    model = Transition
    extra = 0


class IssueAdmin(admin.ModelAdmin):
    list_filter = ['boardposition__board']
    inlines = [
        PositionInline,
        TransitionInline
    ]


admin.site.register(Issue, IssueAdmin)
