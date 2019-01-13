from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Synergy, Turn, Event
from .serializers import TurnSerializer, SynergySerializer, EventSerializer
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

    if author is not None:
        queryset = queryset.filter(author=author)

    return queryset


class TurnViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows cards to be viewed or edited.
  """
  serializer_class = TurnSerializer
  permission_classes = (IsOwner,)

  def get_queryset(self):
    """
    Optionally restricts the returned purchases to a given user,
    by filtering against a `username` query parameter in the URL.
    """
    queryset = Turn.objects.all()
    synergy = self.request.query_params.get('synergy', None)

    if synergy is not None:
        queryset = queryset.filter(synergy=synergy)

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