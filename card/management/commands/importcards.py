from django.core.management.base import BaseCommand, CommandError
from requests import request
import json
from card.models import Card

SET_COUNT = 370

class Command(BaseCommand):
    help = 'Imports cards from json file into db'

    def handle(self, page = 1, *args, **options):
      query_string = {
        'page': page,
        'links': 'cards'
      }
      r = request('get', 'https://www.keyforgegame.com/api/decks/?page=' + str(page) + '&links=cards', params=query_string)
      cards = r.json()['_linked']['cards']

      for card in cards:
        card.pop('is_maverick')

        if (not Card.objects.filter(pk=card['id']).exists()):
          Card.objects.create(**card)
          print(card['id'])

      if Card.objects.all().count() < SET_COUNT:
        self.handle(page + 1, *args, **options)
      else:
        return
