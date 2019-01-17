from django.db import models
from card.models import Card
from enum import Enum

class EventCategory(str, Enum):
  REAP = 'Reap'
  FIGHT = 'Fight'
  ACTION = 'Action'
  PLAY = 'Play'

class Synergy(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def get_owner(self):
    return self.author


class Turn(models.Model):
  synergy = models.ForeignKey('Synergy', related_name='turns', on_delete=models.CASCADE)
  cards = models.ManyToManyField(Card, through='Event')
  rank = models.IntegerField()

  def get_owner(self):
    return self.synergy.author

  class Meta:
    ordering = ('rank',)

class Event(models.Model):
  card = models.ForeignKey('card.Card', related_name='events', on_delete=models.CASCADE)
  turn = models.ForeignKey('Turn', related_name='events', on_delete=models.CASCADE)
  category = models.CharField(
    max_length=6,
    choices=[(tag.value, tag.name) for tag in EventCategory]
  )
  rank = models.IntegerField()

  def get_owner(self):
    return self.turn.synergy.author

  class Meta:
    ordering = ('rank',)
