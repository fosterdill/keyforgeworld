from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import AllowAny
from .models import Card
from .serializers import CardSerializer

class CardViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Card.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CardSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
