from synergy.models import Synergy, Event
from card.serializers import CardSerializer
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import serializers, pagination
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from .models import Synergy, Event

MAX_RELATED_RECORDS = 10

class EventSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)
    card_id = serializers.CharField()
    turn = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = Event
        fields = ('__all__')


    def get_validation_exclusions(self):
        exclusions = super(EventSerializer, self).get_validation_exclusions()
        return exclusions + ['turn', 'card']


class SynergySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Synergy
        fields = '__all__'

    def create(self, validated_data):
        turns = validated_data.pop('turns')
        synergy = Synergy.objects.create(author=self.context['request'].user)

        for turn in turns:
            events = turn.pop('events')

            for event in events:
                Event.objects.create(turn=turn, **event)

        return synergy
        