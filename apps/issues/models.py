from datetime import timedelta
from django.db import models

# Create your models here.
from django.db.models.query import QuerySet
from apps.core.managers import QuerySetManager

class IssueQuerySet(QuerySet):
    def duration_avg(self):
        durations = [i.get_duration() for i in self if i.get_duration()]
        return sum(durations, timedelta()) / len(durations)


class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    objects = QuerySetManager(IssueQuerySet)

    def __unicode__(self):
        return self.name

    def get_first_transition(self):
        return self.transition_set.get(step__initial=True)

    def get_last_transition(self):
        try:
            transition = self.transition_set.get(step__next=None)
        except self.transition_set.model.DoesNotExist:
            transition = None
        return transition

    def get_duration(self):
        if not self.get_last_transition():
            return None
        return self.get_last_transition().date - self.get_first_transition().date

    def get_expected_date(self, time_delta):
        return self.get_first_transition().date + time_delta


