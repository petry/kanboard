from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)

class Story(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board)