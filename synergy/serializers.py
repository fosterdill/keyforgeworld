from synergy.models import Synergy, Turn, Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TurnSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Turn
        fields = '__all__'

class SynergySerializer(serializers.ModelSerializer):
    turns = TurnSerializer(many=True, read_only=True)

    class Meta:
        model = Synergy
        fields = '__all__'