from django.db import models
from card.models import Card
from enum import Enum

class EventCategory(Enum):
  REAP = 'Reap'
  ATTACK = 'Attack'
  ACTION = 'Action'
  PLAY = 'Play'

class Synergy(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Turn(models.Model):
  synergy = models.ForeignKey('Synergy', related_name='turns', on_delete=models.CASCADE)
  cards = models.ManyToManyField(Card, through='Event')
  rank = models.IntegerField()

class Event(models.Model):
  card = models.ForeignKey('card.Card', related_name='events', on_delete=models.CASCADE)
  turn = models.ForeignKey('Turn', related_name='events', on_delete=models.CASCADE)
  category = models.CharField(
    max_length=6,
    choices=[(tag, tag.value) for tag in EventCategory]
  )
  rank = models.IntegerField()
