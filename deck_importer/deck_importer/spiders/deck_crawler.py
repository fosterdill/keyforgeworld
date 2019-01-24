# -*- coding: utf-8 -*-
import scrapy
import json
import re


class DeckCrawlerSpider(scrapy.Spider):
    name = 'deck_crawler'
    allowed_domains = ['keyforgegame.com']
    start_urls = ['https://www.keyforgegame.com/deck-details/']

    def __init__(self, owner, url='', **kwargs):
        self.start_urls = [self.start_urls[0] + url]
        self.owner = owner
        super().__init__(**kwargs)

    def parse(self, response):
        pattern = re.compile(r"__INITIAL_STATE__ = ({.*?});", re.MULTILINE | re.DOTALL)
        payload = response.xpath('//script[contains(., "INITIAL_STATE")]/text()').re(pattern)[0]
        payload = json.loads(payload)

        return {
            'owner': self.owner,
            'deck': payload['decks']['getDeck']['deck'],
        }
