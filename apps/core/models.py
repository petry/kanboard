from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=255)
    next = models.ForeignKey('self', null=True, blank=True)
    initial = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Transition(models.Model):
    story = models.ForeignKey(Story)
    step = models.ForeignKey(Step)
    date = models.DateTimeField(auto_now=True)
