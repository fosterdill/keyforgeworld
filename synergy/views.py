from rest_framework import viewsets, mixins
from django.db.models import Q
from functools import reduce
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Synergy, Event
from deck.models import Deck, DeckEntry
from card.models import Card
from .serializers import SynergySerializer, EventSerializer
from keyforgeworld.permissions import IsOwner

class SynergyViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  serializer_class = SynergySerializer
  permission_classes = (IsOwner,)

  def get_queryset(self):
    """
    Optionally restricts the returned purchases to a given user,
    by filtering against a `username` query parameter in the URL.
    """
    queryset = Synergy.objects.all()
    author = self.request.query_params.get('author', None)
    deck = self.request.query_params.get('deck', None)

    if deck is not None:
        deck = Deck.objects.get(pk=deck)
        synergies = Synergy.objects.exclude(cards__in=Card.objects.exclude(id__in=deck.cards.all()))
        value_list = deck.deck_entries.values_list(
            'entry_card_count', flat=True
        ).distinct()

        group_by_value = {}

        for value in value_list:
            group_by_value[value] = DeckEntry.objects.filter(entry_card_count=value)
        
        queryset = synergies.exclude(reduce(lambda x, y: x | Q(events__card__in=group_by_value[y].values_list('card', flat=True)) & Q(events__event_card_count__gte=(y + 1)), value_list, Q()))

    if author is not None:
        queryset = queryset.filter(author=author)
    
    return queryset


class EventViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = (IsOwner,)

  def get_queryset(self):
    """
    Optionally restricts the returned purchases to a given user,
    by filtering against a `username` query parameter in the URL.
    """
    queryset = Event.objects.all()
    turn = self.request.query_params.get('turn', None)

    if turn is not None:
        queryset = queryset.filter(turn=turn)

    return queryset