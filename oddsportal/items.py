# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OddsportalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    game_time = scrapy.Field()
    game_date = scrapy.Field()
    # away_ht_goal = scrapy.Field()
    # home_ht_goal = scrapy.Field()
    away_ft_goal = scrapy.Field()
    home_ft_goal = scrapy.Field()
    bet_home = scrapy.Field()
    bet_draw = scrapy.Field()
    bet_away = scrapy.Field()