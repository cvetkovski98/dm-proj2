import scrapy
from scraper.items import Song


class SpiderDk(scrapy.Spider):
    name = 'spider_dk'
    start_urls = [
        'http://hitlisten.nu/default.asp?w=15&y=2019&list=a40'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('#basisinfo')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('#artistnavn::text').extract()
            artists = song.css('#titel::text').extract()
            production_house = song.css('a::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = production_house
            chart_position += 1

            yield result
