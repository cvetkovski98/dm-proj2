import scrapy
from scraper.items import Song


class SpiderNor(scrapy.Spider):
    name = 'spider_nor'
    start_urls = [
        'https://www.vglista.no/topplister/topp-20-single-2019-15/'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('.info .wrap')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('.title span::text').extract()
            artists = song.css('.title+ .artist, a::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1

            yield result
