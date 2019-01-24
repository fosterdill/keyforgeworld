# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from deck.models import Deck, DeckEntry

class DeckImporterPipeline(object):
    def process_item(self, data, spider):
        cards_grouped_by_house = data['deck']['cards']
        all_cards = []
        card_counts = {}

        for house, cards_for_house in cards_grouped_by_house.items():
            all_cards += cards_for_house
        
        for card in all_cards:
            card_counts[card['id']] = card_counts[card['id']] if card['id'] in card_counts else 0
            card_counts[card['id']] += 1

        deck = Deck.objects.create(owner_id=data['owner'], name=data['deck']['name'])
        entries = [
            DeckEntry(
                deck=deck, 
                card_id=card['id'], 
                entry_card_count=card_counts[card['id']]
            ) for card in all_cards
        ]
        DeckEntry.objects.bulk_create(entries)
