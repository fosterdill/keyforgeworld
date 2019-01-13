from synergy.models import Synergy, Turn, Event
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import serializers, pagination
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer

MAX_RELATED_RECORDS = 10

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TurnSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = Turn
        fields = '__all__'


    def get_events(self, obj):
        return EventSerializer(Event.objects.all(), many=True).data

class SynergySerializer(serializers.ModelSerializer):
    turns = TurnSerializer(many=True, read_only=True)

    class Meta:
        model = Synergy
        fields = '__all__'