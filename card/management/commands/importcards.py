from django.core.management.base import BaseCommand, CommandError
import json
from card.models import Card

class Command(BaseCommand):
    help = 'Imports cards from json file into db'

    def handle(self, *args, **options):
      with open('card/cards.json') as f:
          cards = json.load(f)

          for card in cards:
            Card(**card).save()