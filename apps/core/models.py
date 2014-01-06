from django.db import models


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


class Story(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=255)
    next = models.ForeignKey('self', null=True, blank=True)
    initial = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class BoardPosition(models.Model):
    story = models.OneToOneField(Story)
    board = models.ForeignKey(Board)
    status = models.ForeignKey('Step')

    def __unicode__(self):
        return "Story #{0} on board {1} in {2}".format(self.story.id, self.board.id, self.status.name)

    def go(self):
        if self.status.next:
            self.status = self.status.next
            self.save()
        return self.status

class Transition(models.Model):
    story = models.ForeignKey(Story)
    step = models.ForeignKey(Step)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "#{0} in {1} on {2}".format(self.story.id, self.step.name, self.date)