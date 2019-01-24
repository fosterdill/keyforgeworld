from django.db import models
from card.models import Card

class Deck(models.Model):
  owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  cards = models.ManyToManyField(Card, through='DeckEntry')

class DeckEntry(models.Model):
  deck = models.ForeignKey('Deck', related_name='deck_entries', on_delete=models.CASCADE)
  card = models.ForeignKey('card.Card', related_name='deck_entries', on_delete=models.CASCADE)
  entry_card_count = models.IntegerField()