import scrapy
from scraper.items import Song


class SpiderFin(scrapy.Spider):
    name = 'spider_fin'
    start_urls = [
        'https://www.ifpi.fi/lista/albumit/2019/15/'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('div.chart-details')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('a.chart-artist::text').extract()
            artists = song.css('a.chart-title::text').extract()
            production_house = song.css('span::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = production_house
            chart_position += 1

            yield result
