import scrapy
import re
from numpy import unique
from bs4 import BeautifulSoup as bs

class oddsportal(scrapy.Spider):
    name = 'oddsportal'
    allowed_domain = [
        ''
    ]
    url = 'http://www.oddsportal.com/soccer/england/premier-league/results/'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=31536000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def start_requests(self):
        print('Now running: %s'% self.name)
        yield scrapy.Request(url=self.url, callback=self.parse)
    
    def base_parse(self, response):
        print('Base parse: %s', response.url)
        years = response.xpath('//*[@id="col-content"]/div[3]/ul/li/span/strong/a/@href').exract()
        print(years)
