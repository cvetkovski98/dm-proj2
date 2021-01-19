import scrapy
from scraper.items import Song


class SpiderUSA(scrapy.Spider):
    name = 'spider_usa'
    start_urls = [
        'https://www.billboard.com/charts/hot-100/2019-04-13'
    ]

    def parse(self, response):
        result = Song()

        songs = response.css('span.chart-element__information')
        chart_position = 1
        for song in songs:
            chart_position = chart_position
            title = song.css('span.chart-element__information__song.text--truncate.color--primary::text').extract()
            artists = song.css(
                'span.chart-element__information__artist.text--truncate.color--secondary::text').extract()

            result['title'] = title
            result['artist'] = artists
            result['chart_position'] = chart_position
            result['production_house'] = None
            chart_position += 1

            yield result
