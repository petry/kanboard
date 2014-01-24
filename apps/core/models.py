from datetime import timedelta
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.query import QuerySet
from apps.core.managers import QuerySetManager


class Board(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def steps(self):
        steps = []
        current_step = self.step_set.get(initial=True)

        while True:
            steps.append(current_step)
            if not current_step.next:
                break
            current_step = current_step.next
        return steps

    def get_absolute_url(self):
        return reverse('board-detail', kwargs={"pk": self.id})


class IssueQuerySet(QuerySet):
    def duration_avg(self):
        durations = [i.get_duration() for i in self if i.get_duration()]
        return sum(durations, timedelta()) / len(durations)


class Issue(models.Model):
    name = models.CharField(max_length=255)
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
        return self.get_first_transition() + time_delta


class Step(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=255)
    next = models.ForeignKey('self', null=True, blank=True)
    initial = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0} - {1}".format(self.board, self.name)


class BoardPosition(models.Model):
    issue = models.OneToOneField(Issue)
    board = models.ForeignKey(Board)
    status = models.ForeignKey('Step', auto_created=True)
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return "Issue #{0} on board {1} in {2}".format(self.issue.id, self.board.id, self.status.name)

    def go(self):
        if self.status.next:
            self.status = self.status.next
            self.save()
            Transition.objects.create(issue=self.issue, step=self.status)
        return self.status


class Transition(models.Model):
    issue = models.ForeignKey(Issue)
    step = models.ForeignKey(Step)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "#{0} in {1} on {2}".format(self.issue.id, self.step.name, self.date)