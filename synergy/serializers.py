from synergy.models import Synergy, Turn
from rest_framework import serializers

class SynergySerializer(serializers.ModelSerializer):
    turns = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Synergy
        fields = ('author', 'turns')


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = ('rank', 'cards')