from django.contrib import admin

# Register your models here.
from apps.core.admin import PositionInline, TransitionInline
from apps.issues.models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_filter = ['boardposition__board']
    inlines = [
        PositionInline,
        TransitionInline
    ]

admin.site.register(Issue, IssueAdmin)
