from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)


class Story(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board)


class Step(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=255)
    next = models.ForeignKey('self')


class Transition(models.Model):
    story = models.ForeignKey(Story)
    step = models.ForeignKey(Step)
    date = models.DateTimeField(auto_now=True)